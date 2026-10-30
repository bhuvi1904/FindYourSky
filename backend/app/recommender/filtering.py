from typing import Dict, Any, List, Tuple
from app.models.entities import School
from app.schemas.questionnaire import QuestionnaireInput

DGCA_RANKING_ORDER = {
    "Category A+": 6,
    "Category A": 5,
    "Category B+": 4,
    "Category B": 3,
    "Category C": 2,
    "Category D": 1,
    "Exempt / Under Assessment": 1,
    "Unranked": 0
}

def evaluate_eligibility(school: School, user_input: QuestionnaireInput) -> Tuple[str, List[str], List[str], List[str]]:
    """
    Evaluates regulatory and operational eligibility for a school against user constraints.
    Returns: (eligibility_status, passed_checks, failed_checks, warnings)
    where eligibility_status is one of: 'verified_eligible', 'eligibility_uncertain', 'not_eligible'
    """
    passed_checks = []
    failed_checks = []
    warnings = []

    # 1. Operational & Regulatory Status
    if school.operational_status == "active":
        passed_checks.append("Active DGCA approval and operational status confirmed.")
    elif school.operational_status == "renewal_in_progress":
        if user_input.allow_unverified:
            warnings.append("DGCA approval renewal in progress; permitted under user flexibility.")
            passed_checks.append("Conditional approval status (Renewal In Progress).")
        else:
            failed_checks.append("Approval renewal in progress; fails strict verification constraint.")
    elif school.operational_status in ["suspended", "ceased"]:
        failed_checks.append(f"FTO regulatory status is {school.operational_status}.")
    else:
        warnings.append("Approval status verification level is pending.")

    # 2. Budget Evaluation
    fee_obj = school.fees[0] if school.fees else None
    if fee_obj and fee_obj.total_estimated_inr > 0:
        total_cost = fee_obj.total_estimated_inr
        if user_input.budget_includes_hostel and not fee_obj.is_fee_inclusive_hostel:
            total_cost += (fee_obj.hostel_mess_annual_inr or 200000.0)

        # Tolerance based on budget flexibility
        tolerance_multiplier = 1.0
        if user_input.budget_flexibility == "moderate":
            tolerance_multiplier = 1.10
        elif user_input.budget_flexibility == "high":
            tolerance_multiplier = 1.25

        effective_max = user_input.max_budget_inr * tolerance_multiplier
        if total_cost <= effective_max:
            passed_checks.append(f"Estimated fee ₹{total_cost:,.0f} is within budget limit (₹{effective_max:,.0f}).")
        else:
            failed_checks.append(f"Estimated fee ₹{total_cost:,.0f} exceeds budget threshold (₹{effective_max:,.0f}).")
    else:
        if user_input.allow_missing_fee:
            warnings.append("Fee data unpublished; permitted under user's missing-fee tolerance.")
            passed_checks.append("Fee data missing but allowed by user preference.")
        else:
            failed_checks.append("Official fee structure unpublished or unverified.")

    # 3. DGCA Ranking Category Filter
    if user_input.min_dgca_category and user_input.min_dgca_category != "Any":
        required_level = DGCA_RANKING_ORDER.get(user_input.min_dgca_category, 0)
        school_rank_obj = school.rankings[0] if school.rankings else None
        school_category = school_rank_obj.ranking_category if school_rank_obj else "Unranked"
        school_level = DGCA_RANKING_ORDER.get(school_category, 0)

        if school_level >= required_level:
            passed_checks.append(f"DGCA ranking {school_category} meets minimum threshold ({user_input.min_dgca_category}).")
        else:
            failed_checks.append(f"DGCA ranking {school_category} is below user required {user_input.min_dgca_category}.")

    # 4. Multi-Engine Requirement
    if user_input.require_multi_engine:
        me_count = sum(fl.operational_count for fl in school.fleet if fl.engine_type == "multi_engine")
        if me_count > 0:
            passed_checks.append(f"Multi-engine training available ({me_count} operational twin-engine aircraft).")
        else:
            failed_checks.append("No operational multi-engine aircraft available in fleet.")

    # 5. Location and Relocation Filter
    if not user_input.willing_to_relocate:
        school_regions = [b.region for b in school.bases]
        school_states = [b.state for b in school.bases]

        region_match = any(r in user_input.preferred_regions for r in school_regions) or "Anywhere" in user_input.preferred_regions
        state_match = any(s in user_input.preferred_states for s in school_states) if user_input.preferred_states else True

        if region_match or state_match:
            passed_checks.append(f"School base located within user's preferred geographic region.")
        else:
            failed_checks.append(f"Bases in {', '.join(set(school_regions))} do not match preferred regions and relocation is declined.")

    # 6. Final Status Determination
    if failed_checks:
        status = "not_eligible"
    elif warnings:
        status = "eligibility_uncertain"
    else:
        status = "verified_eligible"

    return status, passed_checks, failed_checks, warnings
