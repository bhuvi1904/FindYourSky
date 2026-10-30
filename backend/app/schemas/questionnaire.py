from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class PreferenceWeights(BaseModel):
    cost: float = Field(default=0.25, ge=0.0, le=1.0)
    ranking: float = Field(default=0.25, ge=0.0, le=1.0)
    fleet: float = Field(default=0.20, ge=0.0, le=1.0)
    location: float = Field(default=0.15, ge=0.0, le=1.0)
    infrastructure: float = Field(default=0.15, ge=0.0, le=1.0)

class QuestionnaireInput(BaseModel):
    career_objective: str = Field(default="CPL_ME_IR", description="Career goal: CPL, CPL_ME_IR, CADET_PREP, INSTRUCTOR")
    max_budget_inr: float = Field(default=5000000.0, ge=1500000.0, le=15000000.0, description="Max total budget in INR")
    budget_includes_hostel: bool = Field(default=False)
    financing_required: bool = Field(default=False)
    budget_flexibility: str = Field(default="moderate", description="strict, moderate, high")
    preferred_regions: List[str] = Field(default_factory=lambda: ["Anywhere"])
    preferred_states: List[str] = Field(default_factory=list)
    willing_to_relocate: bool = Field(default=True)
    min_dgca_category: str = Field(default="Any", description="Any, Category A+, Category A, Category B+, Category B, Category C")
    require_multi_engine: bool = Field(default=True)
    require_hostel: bool = Field(default=False)
    require_glass_cockpit: bool = Field(default=False)
    require_night_flying: bool = Field(default=False)
    allow_missing_fee: bool = Field(default=False)
    allow_unverified: bool = Field(default=False)
    preset_name: str = Field(default="balanced", description="budget_first, balanced, quality_first, infrastructure, location_first, custom")
    weights: PreferenceWeights = Field(default_factory=PreferenceWeights)

class QuestionnaireValidationResponse(BaseModel):
    is_valid: bool = True
    normalized_weights: Dict[str, float]
    warnings: List[str] = []
    messages: List[str] = []
