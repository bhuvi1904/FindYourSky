from typing import Dict, Any, List, Tuple
from app.models.entities import School
from app.schemas.questionnaire import QuestionnaireInput

CATEGORY_BASE_SCORES = {
    "Category A+": 96.0,
    "Category A": 89.0,
    "Category B+": 82.0,
    "Category B": 75.0,
    "Category C": 60.0,
    "Category D": 54.0,
    "Exempt / Under Assessment": 52.0,
    "Unranked": 50.0
}

def calculate_criterion_scores(school: School, user_input: QuestionnaireInput) -> Dict[str, float]:
    """
    Computes individual normalized criterion scores (0.0 - 100.0) for a given school.
    """
    # 1. Cost Score (Lower comparable cost scores higher)
    fee_obj = school.fees[0] if school.fees else None
    if fee_obj and fee_obj.total_estimated_inr > 0:
        cost = fee_obj.total_estimated_inr
        # Baseline range for Indian FTO CPL: 30 Lakhs (ideal) to 60 Lakhs (expensive)
        min_benchmark = 3000000.0
        max_benchmark = 6000000.0
        clamped_cost = max(min_benchmark, min(max_benchmark, cost))
        # Inverted linear normalization
        cost_score = 100.0 - ((clamped_cost - min_benchmark) / (max_benchmark - min_benchmark)) * 70.0
        # Bonus if significantly under user budget
        if cost < user_input.max_budget_inr:
            savings_pct = (user_input.max_budget_inr - cost) / user_input.max_budget_inr
            cost_score = min(100.0, cost_score + savings_pct * 10.0)
    else:
        cost_score = 50.0 # Neutral disclosure score

    # 2. Ranking Score
    ranking_obj = school.rankings[0] if school.rankings else None
    if ranking_obj:
        cat_score = CATEGORY_BASE_SCORES.get(ranking_obj.ranking_category, 60.0)
        if ranking_obj.overall_score is not None:
            ranking_score = 0.5 * cat_score + 0.5 * ranking_obj.overall_score
        else:
            ranking_score = cat_score
    else:
        ranking_score = 50.0

    # 3. Fleet Score
    total_fleet = sum(fl.operational_count for fl in school.fleet)
    me_fleet = sum(fl.operational_count for fl in school.fleet if fl.engine_type == "multi_engine")
    glass_fleet = sum(fl.operational_count for fl in school.fleet if fl.avionics_type and "Glass" in fl.avionics_type)

    fleet_size_component = min(100.0, (total_fleet / 25.0) * 100.0)
    me_component = min(100.0, (me_fleet / 4.0) * 100.0)
    glass_component = min(100.0, (glass_fleet / max(1, total_fleet)) * 100.0)

    fleet_score = 0.45 * fleet_size_component + 0.35 * me_component + 0.20 * glass_component

    # 4. Location Score
    primary_base = next((b for b in school.bases if b.is_primary), school.bases[0] if school.bases else None)
    if primary_base:
        if user_input.preferred_states and primary_base.state in user_input.preferred_states:
            location_score = 100.0
        elif primary_base.region in user_input.preferred_regions or "Anywhere" in user_input.preferred_regions:
            location_score = 88.0
        elif user_input.willing_to_relocate:
            location_score = 72.0
        else:
            location_score = 35.0
    else:
        location_score = 50.0

    # 5. Infrastructure Score
    infra_points = 50.0 # base
    if primary_base:
        if primary_base.night_flying_available:
            infra_points += 15.0
        if primary_base.runway_length_meters and primary_base.runway_length_meters >= 1800:
            infra_points += 15.0
        elif primary_base.runway_length_meters and primary_base.runway_length_meters >= 1200:
            infra_points += 10.0
        if primary_base.atc_type and ("Controlled" in primary_base.atc_type or "Tower" in primary_base.atc_type):
            infra_points += 10.0
    if fee_obj and fee_obj.is_fee_inclusive_hostel:
        infra_points += 10.0

    infrastructure_score = min(100.0, infra_points)

    return {
        "cost_score": round(cost_score, 1),
        "ranking_score": round(ranking_score, 1),
        "fleet_score": round(fleet_score, 1),
        "location_score": round(location_score, 1),
        "infrastructure_score": round(infrastructure_score, 1)
    }

def generate_explanations(
    school: School,
    subscores: Dict[str, float],
    user_input: QuestionnaireInput,
    budget_gap: float
) -> Tuple[List[str], List[str], List[str]]:
    """
    Generates transparent match reasons, trade-offs, and missing data warnings.
    """
    match_reasons = []
    tradeoffs = []
    missing_info = []

    fee_obj = school.fees[0] if school.fees else None
    ranking_obj = school.rankings[0] if school.rankings else None
    primary_base = next((b for b in school.bases if b.is_primary), school.bases[0] if school.bases else None)

    # Strengths
    if ranking_obj and ranking_obj.ranking_category in ["Category A+", "Category A"]:
        match_reasons.append(f"Premier DGCA {ranking_obj.ranking_category} accredited Flying Training Organisation.")
    if budget_gap >= 0:
        match_reasons.append(f"Highly affordable: fits comfortably within your budget (₹{budget_gap:,.0f} surplus).")
    me_fleet = sum(fl.operational_count for fl in school.fleet if fl.engine_type == "multi_engine")
    if me_fleet >= 2:
        match_reasons.append(f"Substantial dedicated multi-engine fleet ({me_fleet} twin-engine aircraft).")
    if primary_base and primary_base.night_flying_available:
        match_reasons.append(f"Equipped with active runway lighting for full DGCA night-flying requirements.")
    if subscores.get("fleet_score", 0) > 80:
        match_reasons.append("Modern glass-cockpit avionics (Garmin G1000/G3X) aligned with airline standards.")

    # Tradeoffs
    if budget_gap < 0:
        tradeoffs.append(f"Requires budget stretch of ₹{abs(budget_gap):,.0f} above your target ceiling.")
    if ranking_obj and ranking_obj.ranking_category in ["Category C", "Category D"]:
        tradeoffs.append(f"Lower DGCA ranking tier ({ranking_obj.ranking_category}) compared to top-rated academies.")
    if me_fleet == 0:
        tradeoffs.append("No in-house multi-engine aircraft; student must endorse multi-engine rating separately.")
    if primary_base and not primary_base.night_flying_available:
        tradeoffs.append("Night flying not available on base airfield; requires cross-country detachment.")
    if fee_obj and not fee_obj.is_fee_inclusive_hostel:
        tradeoffs.append("Hostel and boarding expenses are billed separately from flight training fees.")

    # Missing / Stale Information
    if not fee_obj or not fee_obj.is_fee_verified:
        missing_info.append("Verified fee breakdown not officially published; quote is based on industry estimates.")
    if school.confidence_score < 0.90:
        missing_info.append(f"Data confidence score is {int(school.confidence_score*100)}%; field verification ongoing.")
    if school.operational_status == "renewal_in_progress":
        missing_info.append("DGCA 5-year FTO approval renewal audit is currently in progress.")

    # Fallbacks if empty
    if not match_reasons:
        match_reasons.append("Meets baseline DGCA flying training syllabus criteria.")
    if not tradeoffs:
        tradeoffs.append("Competitive training option with balanced cost-to-performance profile.")

    return match_reasons, tradeoffs, missing_info
