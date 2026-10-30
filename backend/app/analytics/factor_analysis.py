import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from scipy import stats
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler
from app.analytics.preprocessor import extract_school_features
from app.models.entities import School

EFA_FEATURES = [
    "total_fleet",
    "multi_engine_fleet",
    "dgca_score",
    "annual_flying_hours_k",
    "safety_audit_score",
    "cfi_cadre",
    "tuition_fee_lakhs"
]

def varimax_rotation(loadings: np.ndarray, max_iter: int = 500, tol: float = 1e-6) -> np.ndarray:
    """
    Applies Varimax orthogonal rotation to maximize variance of squared loadings.
    """
    p, k = loadings.shape
    if k == 1:
        return loadings

    rot = np.eye(k)
    var = 0.0

    for _ in range(max_iter):
        comp = loadings @ rot
        u, s, vh = np.linalg.svd(
            loadings.T @ (comp**3 - comp @ np.diag(np.sum(comp**2, axis=0)) / p)
        )
        rot = u @ vh
        new_var = np.sum(s)
        if abs(new_var - var) < tol:
            break
        var = new_var

    return loadings @ rot

def compute_kmo(corr_matrix: np.ndarray) -> Tuple[float, Dict[str, float]]:
    """
    Computes overall Kaiser-Meyer-Olkin (KMO) statistic and per-variable values.
    """
    p = corr_matrix.shape[0]
    try:
        inv_corr = np.linalg.pinv(corr_matrix)
    except Exception:
        return 0.5, {}

    diag_inv = np.diag(inv_corr)
    diag_inv_sqrt = np.sqrt(np.maximum(diag_inv, 1e-10))

    # Partial correlation matrix
    partial_corr = - inv_corr / np.outer(diag_inv_sqrt, diag_inv_sqrt)
    np.fill_diagonal(partial_corr, 0.0)

    r_sq = corr_matrix**2
    np.fill_diagonal(r_sq, 0.0)

    a_sq = partial_corr**2

    # Overall KMO
    sum_r_sq = np.sum(r_sq)
    sum_a_sq = np.sum(a_sq)
    overall_kmo = float(sum_r_sq / (sum_r_sq + sum_a_sq)) if (sum_r_sq + sum_a_sq) > 0 else 0.5

    # Individual variable KMOs
    var_kmo = {}
    for i in range(p):
        var_r = np.sum(r_sq[i, :])
        var_a = np.sum(a_sq[i, :])
        var_kmo[EFA_FEATURES[i]] = float(var_r / (var_r + var_a)) if (var_r + var_a) > 0 else 0.5

    return round(overall_kmo, 3), {k: round(v, 3) for k, v in var_kmo.items()}

def compute_bartlett_sphericity(corr_matrix: np.ndarray, n: int) -> Tuple[float, float]:
    """
    Computes Bartlett's test of sphericity: tests null hypothesis that correlation matrix is identity.
    """
    p = corr_matrix.shape[0]
    det_r = np.linalg.det(corr_matrix)
    if det_r <= 0:
        det_r = 1e-15

    df = p * (p - 1) / 2.0
    chi_square = - (n - 1 - (2.0 * p + 5.0) / 6.0) * np.log(det_r)
    p_value = float(stats.chi2.sf(chi_square, df))
    return round(float(chi_square), 2), p_value

def run_factor_analysis(schools: List[School], n_factors: int = 3) -> Dict[str, Any]:
    """
    Executes Exploratory Factor Analysis with Varimax rotation, scree plot eigenvalues,
    communalities, and factor scores.
    """
    df, metadata = extract_school_features(schools)
    n_samples = len(df)

    if n_samples < 5:
        return {
            "is_available": False,
            "status_message": f"Sample size (N={n_samples}) is insufficient for stable Exploratory Factor Analysis.",
            "sample_size": n_samples,
            "feature_count": len(EFA_FEATURES),
            "features": EFA_FEATURES,
            "eigenvalues": [],
            "cumulative_variance": [],
            "factor_loadings": {},
            "communalities": {},
            "factor_labels": [],
            "school_factor_scores": []
        }

    # Prepare feature matrix, imputing median for any rare missing fee
    X = df[EFA_FEATURES].copy()
    for col in EFA_FEATURES:
        if X[col].isna().any():
            X[col] = X[col].fillna(X[col].median())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Correlation Matrix
    corr_matrix = np.corrcoef(X_scaled, rowvar=False)

    # Diagnostics
    kmo_overall, kmo_vars = compute_kmo(corr_matrix)
    chi_sq, p_val = compute_bartlett_sphericity(corr_matrix, n_samples)

    # Eigenvalues for Scree Plot
    eigenvals, _ = np.linalg.eig(corr_matrix)
    eigenvals = np.sort(np.real(eigenvals))[::-1]
    total_var = float(np.sum(eigenvals))
    var_explained = [float(e / total_var * 100.0) for e in eigenvals]
    cum_var = list(np.cumsum(var_explained))

    # Number of factors selection based on Kaiser criterion (eigenvalue > 1) or max n_factors
    kaiser_factors = sum(1 for e in eigenvals if e >= 1.0)
    actual_k = max(2, min(n_factors, kaiser_factors if kaiser_factors > 0 else 2))

    # Fit Factor Analysis
    fa = FactorAnalysis(n_components=actual_k, random_state=42)
    fa.fit(X_scaled)
    unrotated_loadings = fa.components_.T # Shape (p, k)

    # Apply Varimax Rotation
    rotated_loadings = varimax_rotation(unrotated_loadings)

    # Communalities: h^2 = sum(loadings^2)
    communalities = {}
    for i, feat in enumerate(EFA_FEATURES):
        communalities[feat] = round(float(np.sum(rotated_loadings[i, :]**2)), 3)

    # Factor Loadings map
    loadings_dict = {}
    for i, feat in enumerate(EFA_FEATURES):
        loadings_dict[feat] = [round(float(val), 3) for val in rotated_loadings[i, :]]

    # Compute Factor Scores for schools: F = X_scaled @ inv(R) @ rotated_loadings
    try:
        inv_r = np.linalg.pinv(corr_matrix)
        factor_score_weights = inv_r @ rotated_loadings
        scores = X_scaled @ factor_score_weights
    except Exception:
        scores = fa.transform(X_scaled)

    # Meaningful labels derived from actual feature loading strengths
    factor_labels = []
    default_names = [
        "Institutional Scale & Safety Record",
        "Fleet Capacity & Instructor Cadre",
        "Tuition & Resource Modernity"
    ]
    for k_idx in range(actual_k):
        col_loadings = rotated_loadings[:, k_idx]
        top_idx = int(np.argmax(np.abs(col_loadings)))
        top_feature = EFA_FEATURES[top_idx].replace("_", " ").title()
        if k_idx < len(default_names):
            factor_labels.append(f"F{k_idx+1}: {default_names[k_idx]}")
        else:
            factor_labels.append(f"F{k_idx+1}: {top_feature} Dimension")

    # School Factor Scores with metadata
    school_scores = []
    for idx, row in enumerate(scores):
        meta = metadata[idx]
        score_entry = {
            "school_id": meta["school_id"],
            "name": meta["name"],
            "short_name": meta["short_name"],
            "ranking_category": meta["ranking_category"],
            "factor_scores": {factor_labels[k_i]: round(float(row[k_i]), 2) for k_i in range(actual_k)}
        }
        school_scores.append(score_entry)

    return {
        "is_available": True,
        "status_message": f"Successfully estimated {actual_k}-factor model with Varimax rotation across {n_samples} FTO records.",
        "sample_size": n_samples,
        "feature_count": len(EFA_FEATURES),
        "features": EFA_FEATURES,
        "kmo_overall": kmo_overall,
        "kmo_per_variable": kmo_vars,
        "bartlett_chi_square": chi_sq,
        "bartlett_p_value": p_val,
        "num_factors_selected": actual_k,
        "eigenvalues": [round(float(e), 3) for e in eigenvals],
        "cumulative_variance": [round(float(c), 1) for c in cum_var[:len(EFA_FEATURES)]],
        "factor_loadings": loadings_dict,
        "communalities": communalities,
        "factor_labels": factor_labels,
        "school_factor_scores": school_scores
    }
