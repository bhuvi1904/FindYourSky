from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from app.schemas.questionnaire import QuestionnaireInput

class SchoolMatchResult(BaseModel):
    school_id: str
    name: str
    short_name: Optional[str] = None
    slug: str
    website_url: str
    primary_city: str
    primary_state: str
    primary_region: str
    rank: int
    overall_match_score: float # 0 to 100
    regulatory_eligibility: str # verified_eligible, eligibility_uncertain, not_eligible
    
    # Sub-scores
    cost_score: float
    ranking_score: float
    fleet_score: float
    location_score: float
    infrastructure_score: float
    statistical_boost: float = 0.0
    
    # Financial details
    indicative_fee_inr: Optional[float] = None
    is_fee_verified: bool = False
    fee_inclusions: List[str] = []
    fee_exclusions: List[str] = []
    budget_gap_inr: float = 0.0 # Positive if within budget, negative if over budget
    
    # Operational & Fleet
    dgca_ranking_category: str
    dgca_overall_score: Optional[float] = None
    total_fleet_count: int
    multi_engine_count: int
    aircraft_models: List[str] = []
    night_flying_available: bool
    atc_environment: Optional[str] = None
    
    # Explanations
    match_reasons: List[str] = []
    tradeoffs: List[str] = []
    missing_information: List[str] = []
    
    # Provenance
    dgca_approval_no: str
    approval_validity: Optional[str] = None
    last_verified_date: Optional[str] = None
    confidence_score: float
    completeness_score: float
    dgca_document_url: Optional[str] = None
    is_synthetic: bool = False

class RecommendationResponse(BaseModel):
    run_id: str
    analytical_mode: str # hybrid, logistic_regression, factor_analysis, clustering
    total_evaluated: int
    eligible_count: int
    schools: List[SchoolMatchResult]
    methodology_summary: str
    weights_applied: Dict[str, float]
    sensitivity_analysis: Optional[Dict[str, List[Dict[str, Any]]]] = None

class SchoolComparisonRequest(BaseModel):
    school_ids: List[str] = Field(..., min_items=2, max_items=5)
    questionnaire: Optional[QuestionnaireInput] = None

class ComparisonMetricRow(BaseModel):
    metric_label: str
    category: str # Regulatory, Fleet, Financial, Training, Quality
    values: Dict[str, Optional[str]]
    highlight_best_id: Optional[str] = None
    data_verified: Dict[str, bool] = {}

class SchoolComparisonResponse(BaseModel):
    schools: List[SchoolMatchResult]
    comparison_table: List[ComparisonMetricRow]
    tradeoff_matrix: Dict[str, List[str]]
