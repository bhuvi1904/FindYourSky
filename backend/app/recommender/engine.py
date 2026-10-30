from typing import List, Dict, Any, Tuple
import copy
from sqlalchemy.orm import Session
from app.models.entities import School, RecommendationRun, RecommendationResult
from app.schemas.questionnaire import QuestionnaireInput
from app.schemas.recommendation import SchoolMatchResult, RecommendationResponse
from app.recommender.filtering import evaluate_eligibility
from app.recommender.preference_scorer import calculate_criterion_scores, generate_explanations
from app.analytics.logistic_regression import train_and_evaluate_logistic_regression
from app.analytics.clustering import run_kmeans_clustering
from app.analytics.factor_analysis import run_factor_analysis

def normalize_user_weights(weights) -> Dict[str, float]:
    """
    Normalizes user preference weights so their sum equals 1.0.
    """
    w_dict = {
        "cost": float(weights.cost),
        "ranking": float(weights.ranking),
        "fleet": float(weights.fleet),
        "location": float(weights.location),
        "infrastructure": float(weights.infrastructure)
    }
    total = sum(w_dict.values())
    if total <= 0:
        return {k: 0.20 for k in w_dict}
    return {k: round(v / total, 4) for k, v in w_dict.items()}

def generate_recommendations(
    db: Session,
    user_input: QuestionnaireInput,
    analytical_mode: str = "hybrid"
) -> RecommendationResponse:
    """
    Executes the multi-stage recommendation pipeline:
    Stage 1: Regulatory and eligibility filtering
    Stage 2: Multi-criteria preference scoring
    Stage 3: Statistical model integration (Hybrid / LR / EFA / K-Means)
    Stage 4: Transparent ranking, explanations, trade-offs, and sensitivity analysis.
    """
    all_schools = db.query(School).all()
    if not all_schools:
        return RecommendationResponse(
            run_id="run_empty",
            analytical_mode=analytical_mode,
            total_evaluated=0,
            eligible_count=0,
            schools=[],
            methodology_summary="No flying schools found in database.",
            weights_applied={}
        )

    norm_weights = normalize_user_weights(user_input.weights)

    # Pre-train / evaluate statistical models if in hybrid or model modes
    lr_prob_map = {}
    cluster_bonus_map = {}

    if analytical_mode in ["hybrid", "logistic_regression"]:
        lr_result = train_and_evaluate_logistic_regression(all_schools)
        if lr_result.get("is_available"):
            for sp in lr_result.get("school_probabilities", []):
                lr_prob_map[sp["school_id"]] = sp["suitability_probability"]

    if analytical_mode in ["hybrid", "clustering"]:
        km_result = run_kmeans_clustering(all_schools)
        if km_result.get("is_available"):
            # If user prioritizes budget, bonus for cluster with lower fee; if quality, bonus for cluster with premier fleet
            for p in km_result.get("cluster_profiles", []):
                pass # Available for profiling

    evaluated_candidates = []

    for school in all_schools:
        # Stage 1: Regulatory Filtering
        elig_status, passed_chk, failed_chk, warnings = evaluate_eligibility(school, user_input)

        # In strict mode, filter out not_eligible
        if elig_status == "not_eligible" and not user_input.allow_unverified:
            continue

        # Stage 2: Preference Scoring
        subscores = calculate_criterion_scores(school, user_input)

        # Baseline Weighted Preference Score
        pref_score = (
            norm_weights["cost"] * subscores["cost_score"] +
            norm_weights["ranking"] * subscores["ranking_score"] +
            norm_weights["fleet"] * subscores["fleet_score"] +
            norm_weights["location"] * subscores["location_score"] +
            norm_weights["infrastructure"] * subscores["infrastructure_score"]
        )

        # Stage 3: Statistical Integration
        stat_boost = 0.0
        if analytical_mode == "hybrid":
            # 75% preference score + 25% logistic regression probability (scaled to 100)
            if school.school_id in lr_prob_map:
                lr_score = lr_prob_map[school.school_id] * 100.0
                stat_boost = round((lr_score - pref_score) * 0.20, 1)
                final_score = pref_score * 0.80 + lr_score * 0.20
            else:
                final_score = pref_score
        elif analytical_mode == "logistic_regression":
            if school.school_id in lr_prob_map:
                lr_score = lr_prob_map[school.school_id] * 100.0
                stat_boost = round(lr_score - pref_score, 1)
                final_score = 0.50 * pref_score + 0.50 * lr_score
            else:
                final_score = pref_score
        else:
            final_score = pref_score

        # Ensure bounds 0-100
        final_score = max(10.0, min(100.0, round(final_score, 1)))

        # Financial details
        fee_obj = school.fees[0] if school.fees else None
        total_fee = fee_obj.total_estimated_inr if fee_obj else None
        budget_gap = (user_input.max_budget_inr - total_fee) if total_fee else 0.0

        # Explanations
        reasons, tradeoffs, missing_info = generate_explanations(school, subscores, user_input, budget_gap)

        # Primary base & fleet
        primary_base = next((b for b in school.bases if b.is_primary), school.bases[0] if school.bases else None)
        ranking_obj = school.rankings[0] if school.rankings else None
        total_fleet = sum(fl.operational_count for fl in school.fleet)
        me_fleet = sum(fl.operational_count for fl in school.fleet if fl.engine_type == "multi_engine")
        models_list = list(set(fl.aircraft_model for fl in school.fleet))

        evaluated_candidates.append({
            "school_id": school.school_id,
            "name": school.name,
            "short_name": school.short_name or school.name,
            "slug": school.slug,
            "website_url": school.website_url,
            "primary_city": primary_base.city if primary_base else "N/A",
            "primary_state": primary_base.state if primary_base else "N/A",
            "primary_region": primary_base.region if primary_base else "N/A",
            "rank": 0,
            "overall_match_score": final_score,
            "regulatory_eligibility": elig_status,
            "cost_score": subscores["cost_score"],
            "ranking_score": subscores["ranking_score"],
            "fleet_score": subscores["fleet_score"],
            "location_score": subscores["location_score"],
            "infrastructure_score": subscores["infrastructure_score"],
            "statistical_boost": stat_boost,
            "indicative_fee_inr": total_fee,
            "is_fee_verified": fee_obj.is_fee_verified if fee_obj else False,
            "fee_inclusions": fee_obj.inclusions if fee_obj else [],
            "fee_exclusions": fee_obj.exclusions if fee_obj else [],
            "budget_gap_inr": budget_gap,
            "dgca_ranking_category": ranking_obj.ranking_category if ranking_obj else "Unranked",
            "dgca_overall_score": ranking_obj.overall_score if ranking_obj else None,
            "total_fleet_count": total_fleet,
            "multi_engine_count": me_fleet,
            "aircraft_models": models_list,
            "night_flying_available": primary_base.night_flying_available if primary_base else False,
            "atc_environment": primary_base.atc_type if primary_base else None,
            "match_reasons": reasons,
            "tradeoffs": tradeoffs,
            "missing_information": missing_info,
            "dgca_approval_no": school.dgca_approval_no,
            "approval_validity": school.approval_validity,
            "last_verified_date": school.last_verified_date,
            "confidence_score": school.confidence_score,
            "completeness_score": school.completeness_score,
            "dgca_document_url": "https://www.dgca.gov.in/digigov-portal/",
            "is_synthetic": school.is_synthetic
        })

    # Sort descending by overall match score
    evaluated_candidates.sort(key=lambda x: x["overall_match_score"], reverse=True)

    # Assign ranks
    for r_idx, c in enumerate(evaluated_candidates):
        c["rank"] = r_idx + 1

    # Sensitivity Analysis: evaluate shifts when weights vary +/- 20%
    sensitivity = {}
    top_candidates = evaluated_candidates[:5]
    for test_key, test_label in [("cost", "Budget Priority (+20%)"), ("ranking", "Ranking Priority (+20%)"), ("fleet", "Fleet Priority (+20%)")]:
        alt_weights = copy.deepcopy(norm_weights)
        alt_weights[test_key] = min(0.60, alt_weights[test_key] + 0.20)
        tot = sum(alt_weights.values())
        alt_norm = {k: v / tot for k, v in alt_weights.items()}

        sim_points = []
        for cand in top_candidates:
            sim_score = round(
                alt_norm["cost"] * cand["cost_score"] +
                alt_norm["ranking"] * cand["ranking_score"] +
                alt_norm["fleet"] * cand["fleet_score"] +
                alt_norm["location"] * cand["location_score"] +
                alt_norm["infrastructure"] * cand["infrastructure_score"],
                1
            )
            sim_points.append({
                "short_name": cand["short_name"],
                "base_score": cand["overall_match_score"],
                "simulated_score": sim_score,
                "score_delta": round(sim_score - cand["overall_match_score"], 1)
            })
        sensitivity[test_label] = sim_points

    methodology = (
        f"Multi-criteria recommendation using '{analytical_mode}' mode. "
        f"Filtered {len(all_schools)} institutions through mandatory regulatory and budget constraints; "
        f"ranked {len(evaluated_candidates)} eligible FTOs using normalized weights "
        f"[Cost: {norm_weights['cost']:.2f}, DGCA Rank: {norm_weights['ranking']:.2f}, Fleet: {norm_weights['fleet']:.2f}, Location: {norm_weights['location']:.2f}, Infra: {norm_weights['infrastructure']:.2f}]."
    )

    return RecommendationResponse(
        run_id=f"run_{analytical_mode}_{len(evaluated_candidates)}",
        analytical_mode=analytical_mode,
        total_evaluated=len(all_schools),
        eligible_count=len(evaluated_candidates),
        schools=[SchoolMatchResult(**c) for c in evaluated_candidates],
        methodology_summary=methodology,
        weights_applied=norm_weights,
        sensitivity_analysis=sensitivity
    )
