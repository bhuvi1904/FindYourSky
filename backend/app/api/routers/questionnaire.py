from fastapi import APIRouter
from app.schemas.questionnaire import QuestionnaireInput, QuestionnaireValidationResponse
from app.recommender.engine import normalize_user_weights

router = APIRouter(prefix="/questionnaire", tags=["Questionnaire"])

@router.post("/validate", response_model=QuestionnaireValidationResponse)
def validate_questionnaire(data: QuestionnaireInput):
    """
    Validates questionnaire constraints, checks budget feasibility for Indian CPL,
    and returns normalized preference weights.
    """
    warnings = []
    messages = []
    normalized = normalize_user_weights(data.weights)

    if data.max_budget_inr < 3200000:
        warnings.append(
            f"Budget of ₹{data.max_budget_inr:,.0f} is below average commercial pilot training costs in India (typically ₹35L - ₹55L). Eligible options will be restricted to state-subsidized flying clubs."
        )

    if not data.willing_to_relocate and (not data.preferred_regions or "Anywhere" in data.preferred_regions):
        warnings.append("You indicated unwillingness to relocate but selected 'Anywhere' as region. Please specify preferred states.")

    if data.require_multi_engine and data.max_budget_inr < 3800000:
        warnings.append("Multi-engine flight training usually requires a budget above ₹40 Lakhs due to twin-engine fuel and maintenance costs.")

    messages.append("Questionnaire validation passed successfully.")

    return QuestionnaireValidationResponse(
        is_valid=True,
        normalized_weights=normalized,
        warnings=warnings,
        messages=messages
    )
