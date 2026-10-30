import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score
from app.analytics.preprocessor import extract_school_features
from app.models.entities import School

CLUSTER_FEATURES = [
    "tuition_fee_lakhs",
    "total_fleet",
    "multi_engine_fleet",
    "dgca_score",
    "annual_flying_hours_k",
    "safety_audit_score",
    "night_flying",
    "runway_length_km"
]

def run_kmeans_clustering(schools: List[School], fixed_k: int = None) -> Dict[str, Any]:
    """
    Executes diagnostic K-Means clustering across candidate values of K (2..5),
    computes inertia and silhouette scores, selects optimal K, profiles centroids,
    and calculates 2D PCA projection coordinates.
    """
    df, metadata = extract_school_features(schools)
    n_samples = len(df)

    if n_samples < 4:
        return {
            "is_available": False,
            "status_message": f"Sample size (N={n_samples}) is insufficient for reliable K-Means clustering.",
            "optimal_k": 2,
            "candidate_k_values": [],
            "inertias": [],
            "silhouette_scores": [],
            "cluster_profiles": [],
            "school_cluster_assignments": [],
            "pca_2d_points": [],
            "stability_score": 0.0
        }

    # Clean and scale features
    X = df[CLUSTER_FEATURES].copy()
    for col in CLUSTER_FEATURES:
        if X[col].isna().any():
            X[col] = X[col].fillna(X[col].median())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Diagnostic sweep over K = 2 to min(5, n_samples - 1)
    max_k = min(5, n_samples - 1)
    candidate_k = list(range(2, max_k + 1))
    inertias = []
    silhouettes = []

    models = {}
    for k in candidate_k:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X_scaled)
        inertias.append(round(float(km.inertia_), 2))
        sil = float(silhouette_score(X_scaled, labels))
        silhouettes.append(round(sil, 3))
        models[k] = (km, labels)

    # Determine optimal K
    if fixed_k and fixed_k in candidate_k:
        optimal_k = fixed_k
    else:
        best_idx = int(np.argmax(silhouettes))
        optimal_k = candidate_k[best_idx]

    best_km, best_labels = models[optimal_k]

    # Cluster Profiles & Semantic Archetypes from actual centroids
    cluster_profiles = []
    for c_id in range(optimal_k):
        mask = (best_labels == c_id)
        cluster_df = X[mask]
        cluster_size = int(np.sum(mask))

        mean_fee = float(cluster_df["tuition_fee_lakhs"].mean())
        mean_fleet = float(cluster_df["total_fleet"].mean())
        mean_me = float(cluster_df["multi_engine_fleet"].mean())
        mean_dgca = float(cluster_df["dgca_score"].mean())
        mean_hours = float(cluster_df["annual_flying_hours_k"].mean())
        night_pct = float(cluster_df["night_flying"].mean() * 100.0)

        # Interpret cluster characteristics based on real centroids
        if mean_fleet >= 15.0 and mean_me >= 2.0:
            archetype_name = "Premier Large-Scale Multi-Engine Academies"
            archetype_desc = f"Large active fleet (mean {mean_fleet:.1f} aircraft), dedicated multi-engine assets, high DGCA audit score ({mean_dgca:.1f}), comprehensive night flying infrastructure."
        elif mean_fee <= 38.0:
            archetype_name = "Affordable Regional & Subsidized Flight Clubs"
            archetype_desc = f"Budget-friendly tuition (mean ₹{mean_fee:.1f} Lakhs), reliable single-engine fleet (mean {mean_fleet:.1f}), predominantly state-funded or trust-operated."
        else:
            archetype_name = "Balanced Commercial Pilot Pathways"
            archetype_desc = f"Moderate fees (mean ₹{mean_fee:.1f} Lakhs), modern trainer fleet (mean {mean_fleet:.1f}), strong regional placement record."

        cluster_profiles.append({
            "cluster_id": c_id,
            "cluster_name": f"Cluster {c_id + 1}: {archetype_name}",
            "description": archetype_desc,
            "size": cluster_size,
            "percentage": round(cluster_size / n_samples * 100.0, 1),
            "mean_tuition_fee_lakhs": round(mean_fee, 1),
            "mean_fleet_size": round(mean_fleet, 1),
            "mean_multi_engine_count": round(mean_me, 1),
            "mean_dgca_score": round(mean_dgca, 1),
            "mean_annual_hours_k": round(mean_hours, 1),
            "night_flying_available_pct": round(night_pct, 1)
        })

    # PCA 2D projection for visualization
    pca = PCA(n_components=2, random_state=42)
    coords_2d = pca.fit_transform(X_scaled)
    pca_points = []
    assignments = []

    for idx in range(n_samples):
        meta = metadata[idx]
        assigned_cluster = int(best_labels[idx])
        profile = cluster_profiles[assigned_cluster]

        point = {
            "school_id": meta["school_id"],
            "name": meta["name"],
            "short_name": meta["short_name"],
            "cluster_id": assigned_cluster,
            "cluster_name": profile["cluster_name"],
            "pca_x": round(float(coords_2d[idx, 0]), 3),
            "pca_y": round(float(coords_2d[idx, 1]), 3),
            "ranking_category": meta["ranking_category"],
            "fee_lakhs": round(float(X.iloc[idx]["tuition_fee_lakhs"]), 1),
            "fleet_size": int(X.iloc[idx]["total_fleet"])
        }
        pca_points.append(point)
        assignments.append({
            "school_id": meta["school_id"],
            "name": meta["name"],
            "cluster_id": assigned_cluster,
            "cluster_name": profile["cluster_name"]
        })

    # Stability across random seeds
    seeds = [0, 10, 42, 100, 2026]
    ari_scores = []
    for s in seeds:
        km_s = KMeans(n_clusters=optimal_k, random_state=s, n_init=5)
        labels_s = km_s.fit_predict(X_scaled)
        ari = adjusted_rand_score(best_labels, labels_s)
        ari_scores.append(ari)
    stability_score = round(float(np.mean(ari_scores)), 3)

    return {
        "is_available": True,
        "status_message": f"K-Means clustering converged with optimal K={optimal_k} (Silhouette={max(silhouettes):.3f}, Stability={stability_score:.3f}).",
        "optimal_k": optimal_k,
        "candidate_k_values": candidate_k,
        "inertias": inertias,
        "silhouette_scores": silhouettes,
        "cluster_profiles": cluster_profiles,
        "school_cluster_assignments": assignments,
        "pca_2d_points": pca_points,
        "stability_score": stability_score
    }
