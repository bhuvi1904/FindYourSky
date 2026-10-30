from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.db.session import get_db
from app.models.entities import School, QuestionnaireResponse, RecommendationRun
from app.schemas.questionnaire import QuestionnaireInput
from app.schemas.recommendation import (
    RecommendationResponse, SchoolComparisonRequest, SchoolComparisonResponse, ComparisonMetricRow
)
from app.recommender.engine import generate_recommendations

router = APIRouter(prefix="/recommendations", tags=["Recommendation Engine"])

@router.post("", response_model=RecommendationResponse)
def get_recommendations(
    user_input: QuestionnaireInput,
    mode: str = Query("hybrid", description="Analytical mode: hybrid, logistic_regression, factor_analysis, clustering"),
    db: Session = Depends(get_db)
):
    """
    Executes the multi-stage recommendation pipeline and returns ranked shortlist
    with score breakdowns, explanations, and trade-offs.
    """
    return generate_recommendations(db, user_input, analytical_mode=mode)

@router.post("/compare", response_model=SchoolComparisonResponse)
def compare_schools(
    request: SchoolComparisonRequest,
    db: Session = Depends(get_db)
):
    """
    Compares 2 to 5 selected schools across official DGCA ranking, verified fees,
    fleet size, multi-engine capacity, runway and infrastructure.
    """
    schools = db.query(School).filter(School.school_id.in_(request.school_ids)).all()
    if len(schools) < 2:
        raise HTTPException(status_code=400, detail="Please select at least 2 schools for comparison.")

    # Re-evaluate schools with default or provided questionnaire, ensuring selected schools are not filtered out by strict budget
    q_input = request.questionnaire or QuestionnaireInput()
    q_input.allow_unverified = True
    q_input.budget_flexibility = "high"
    q_input.max_budget_inr = max(q_input.max_budget_inr, 10000000.0)
    rec_resp = generate_recommendations(db, q_input, analytical_mode="hybrid")
    school_matches = [s for s in rec_resp.schools if s.school_id in request.school_ids]

    # Build comparison rows
    comparison_table = []

    # Row 1: DGCA Category
    cat_vals = {}
    ver_status = {}
    for s in school_matches:
        cat_vals[s.school_id] = s.dgca_ranking_category
        ver_status[s.school_id] = True
    comparison_table.append(ComparisonMetricRow(
        metric_label="DGCA Ranking Category",
        category="Regulatory",
        values=cat_vals,
        data_verified=ver_status
    ))

    # Row 2: DGCA Score
    score_vals = {}
    for s in school_matches:
        score_vals[s.school_id] = f"{s.dgca_overall_score:.1f}/100" if s.dgca_overall_score else "Not Verified"
        ver_status[s.school_id] = (s.dgca_overall_score is not None)
    comparison_table.append(ComparisonMetricRow(
        metric_label="DGCA Performance Score",
        category="Regulatory",
        values=score_vals,
        data_verified=ver_status
    ))

    # Row 3: Total Fee
    fee_vals = {}
    for s in school_matches:
        fee_vals[s.school_id] = f"₹{s.indicative_fee_inr:,.0f}" if s.indicative_fee_inr else "Not Verified"
        ver_status[s.school_id] = s.is_fee_verified
    comparison_table.append(ComparisonMetricRow(
        metric_label="Total Estimated CPL Fee",
        category="Financial",
        values=fee_vals,
        data_verified=ver_status
    ))

    # Row 4: Fleet Size
    fleet_vals = {}
    for s in school_matches:
        fleet_vals[s.school_id] = f"{s.total_fleet_count} Aircraft"
        ver_status[s.school_id] = True
    comparison_table.append(ComparisonMetricRow(
        metric_label="Active Fleet Size",
        category="Fleet",
        values=fleet_vals,
        data_verified=ver_status
    ))

    # Row 5: Multi-Engine Count
    me_vals = {}
    for s in school_matches:
        me_vals[s.school_id] = f"{s.multi_engine_count} Twin-Engine" if s.multi_engine_count > 0 else "None (Single Only)"
        ver_status[s.school_id] = True
    comparison_table.append(ComparisonMetricRow(
        metric_label="Multi-Engine Trainers",
        category="Fleet",
        values=me_vals,
        data_verified=ver_status
    ))

    # Row 6: Location
    loc_vals = {}
    for s in school_matches:
        loc_vals[s.school_id] = f"{s.primary_city}, {s.primary_state}"
        ver_status[s.school_id] = True
    comparison_table.append(ComparisonMetricRow(
        metric_label="Primary Training Base",
        category="Infrastructure",
        values=loc_vals,
        data_verified=ver_status
    ))

    # Row 7: Night Flying
    night_vals = {}
    for s in school_matches:
        night_vals[s.school_id] = "Available On Base" if s.night_flying_available else "Requires Detachment"
        ver_status[s.school_id] = True
    comparison_table.append(ComparisonMetricRow(
        metric_label="Night Flying Lighting",
        category="Infrastructure",
        values=night_vals,
        data_verified=ver_status
    ))

    # Trade-off matrix
    tradeoffs_matrix = {}
    for s in school_matches:
        tradeoffs_matrix[s.school_id] = s.tradeoffs

    return SchoolComparisonResponse(
        schools=school_matches,
        comparison_table=comparison_table,
        tradeoff_matrix=tradeoffs_matrix
    )
