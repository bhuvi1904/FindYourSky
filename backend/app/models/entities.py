from datetime import datetime
import json
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
)
from sqlalchemy.orm import relationship
from app.db.session import Base

# 1. schools
class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(String(64), unique=True, index=True, nullable=False) # e.g. FTO_IGRUA_001
    name = Column(String(255), index=True, nullable=False)
    short_name = Column(String(64), index=True, nullable=True)
    slug = Column(String(128), unique=True, index=True, nullable=False)
    website_url = Column(String(512), nullable=False)
    ownership_type = Column(String(64), index=True, nullable=False) # autonomous_government, private, joint_venture, state_government, trust_historical, university_women
    dgca_approval_no = Column(String(128), nullable=False)
    approval_validity = Column(String(32), nullable=True)
    operational_status = Column(String(32), default="active", index=True) # active, renewal_in_progress, suspended, unverified
    established_year = Column(Integer, nullable=True)
    confidence_score = Column(Float, default=1.0)
    completeness_score = Column(Float, default=1.0)
    last_verified_date = Column(String(32), nullable=True)
    is_synthetic = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    bases = relationship("SchoolBase", back_populates="school", cascade="all, delete-orphan")
    fleet = relationship("AircraftFleet", back_populates="school", cascade="all, delete-orphan")
    fees = relationship("SchoolFee", back_populates="school", cascade="all, delete-orphan")
    rankings = relationship("DGCARanking", back_populates="school", cascade="all, delete-orphan")
    programmes = relationship("SchoolProgramme", back_populates="school", cascade="all, delete-orphan")
    source_observations = relationship("SourceObservation", back_populates="school", cascade="all, delete-orphan")
    recommendation_results = relationship("RecommendationResult", back_populates="school")


# 2. school_bases
class SchoolBase(Base):
    __tablename__ = "school_bases"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    base_id = Column(String(64), nullable=False)
    is_primary = Column(Boolean, default=False)
    airport_name = Column(String(255), nullable=False)
    icao_code = Column(String(16), nullable=True, index=True)
    city = Column(String(128), nullable=False, index=True)
    state = Column(String(128), nullable=False, index=True)
    region = Column(String(32), nullable=False, index=True) # North, South, East, West, Central, North-East
    runway_length_meters = Column(Integer, nullable=True)
    runway_surface = Column(String(64), nullable=True)
    night_flying_available = Column(Boolean, default=False)
    atc_type = Column(String(128), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    school = relationship("School", back_populates="bases")


# 3. aircraft_fleet
class AircraftFleet(Base):
    __tablename__ = "aircraft_fleet"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    aircraft_model = Column(String(128), nullable=False)
    manufacturer = Column(String(128), nullable=True)
    engine_type = Column(String(32), nullable=False, index=True) # single_engine, multi_engine
    avionics_type = Column(String(128), nullable=True) # Glass Cockpit, Analogue, Hybrid
    count = Column(Integer, default=1)
    operational_count = Column(Integer, default=1)
    fuel_type = Column(String(64), nullable=True)

    school = relationship("School", back_populates="fleet")


# 4. school_fees
class SchoolFee(Base):
    __tablename__ = "school_fees"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    course_name = Column(String(255), nullable=False)
    currency = Column(String(8), default="INR")
    tuition_flying_inr = Column(Float, nullable=False)
    ground_school_inr = Column(Float, default=0.0)
    simulator_inr = Column(Float, default=0.0)
    hostel_mess_annual_inr = Column(Float, default=0.0)
    tax_gst_inr = Column(Float, default=0.0)
    total_estimated_inr = Column(Float, nullable=False, index=True)
    is_fee_inclusive_hostel = Column(Boolean, default=False)
    is_fee_verified = Column(Boolean, default=False, index=True)
    fee_effective_date = Column(String(32), nullable=True)
    source_url = Column(String(512), nullable=True)
    inclusions_json = Column(Text, nullable=True) # JSON list
    exclusions_json = Column(Text, nullable=True) # JSON list
    notes = Column(Text, nullable=True)

    school = relationship("School", back_populates="fees")

    @property
    def inclusions(self):
        return json.loads(self.inclusions_json) if self.inclusions_json else []

    @property
    def exclusions(self):
        return json.loads(self.exclusions_json) if self.exclusions_json else []


# 5. dgca_rankings
class DGCARanking(Base):
    __tablename__ = "dgca_rankings"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    ranking_period = Column(String(32), nullable=False, index=True) # e.g. 2025-2026, April 2026
    ranking_category = Column(String(32), nullable=False, index=True) # Category A+, Category A, Category B+, Category B, Category C, Category D
    overall_score = Column(Float, nullable=True) # 0 to 100
    national_rank = Column(Integer, nullable=True)
    annual_hours_logged = Column(Float, nullable=True)
    safety_audit_score = Column(Float, nullable=True)
    cfi_cadre_strength = Column(Integer, nullable=True)
    source_id = Column(String(64), nullable=True)
    effective_date = Column(String(32), nullable=True)
    notes = Column(Text, nullable=True)

    school = relationship("School", back_populates="rankings")


# 6. data_sources
class DataSource(Base):
    __tablename__ = "data_sources"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String(64), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    url = Column(String(512), nullable=False)
    source_type = Column(String(64), nullable=False) # official_regulator, official_ministry, official_portal, official_notice, school_website, independent
    publisher = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    verification_status = Column(String(32), default="verified", index=True)
    retrieval_date = Column(String(32), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    observations = relationship("SourceObservation", back_populates="source")


# 7. source_observations
class SourceObservation(Base):
    __tablename__ = "source_observations"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    source_id = Column(Integer, ForeignKey("data_sources.id", ondelete="CASCADE"), nullable=False, index=True)
    field_name = Column(String(64), nullable=False, index=True)
    observed_value = Column(Text, nullable=True)
    verification_status = Column(String(32), default="official") # official, school_published, independently_reported, estimated, missing
    confidence_level = Column(Float, default=1.0)
    observation_date = Column(String(32), nullable=True)
    retrieval_date = Column(String(32), nullable=True)
    source_url = Column(String(512), nullable=True)

    school = relationship("School", back_populates="source_observations")
    source = relationship("DataSource", back_populates="observations")


# 8. school_programmes
class SchoolProgramme(Base):
    __tablename__ = "school_programmes"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    programme_name = Column(String(255), nullable=False)
    licence_type = Column(String(64), default="CPL") # CPL, PPL, Multi-Engine, IR, AFIR, Degree
    duration_months = Column(Integer, default=15)
    description = Column(Text, nullable=True)

    school = relationship("School", back_populates="programmes")


# 9. questionnaire_responses
class QuestionnaireResponse(Base):
    __tablename__ = "questionnaire_responses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(64), unique=True, index=True, nullable=False)
    career_objective = Column(String(64), default="CPL_ME_IR") # CPL, CPL_ME_IR, CADET_PREP, INSTRUCTOR
    max_budget_inr = Column(Float, nullable=False)
    budget_includes_hostel = Column(Boolean, default=False)
    financing_required = Column(Boolean, default=False)
    budget_flexibility = Column(String(32), default="moderate") # strict, moderate, high
    preferred_regions_json = Column(Text, nullable=True) # ["North", "South", "Anywhere"]
    preferred_states_json = Column(Text, nullable=True)
    willing_to_relocate = Column(Boolean, default=True)
    preset_name = Column(String(64), default="balanced") # budget_first, balanced, quality_first, infrastructure, location_first, custom
    weights_json = Column(Text, nullable=False) # JSON weights dictionary
    aircraft_preferences_json = Column(Text, nullable=True)
    min_dgca_category = Column(String(32), default="Any")
    require_multi_engine = Column(Boolean, default=True)
    require_hostel = Column(Boolean, default=False)
    allow_missing_fee = Column(Boolean, default=False)
    allow_unverified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    runs = relationship("RecommendationRun", back_populates="questionnaire")


# 10. recommendation_runs
class RecommendationRun(Base):
    __tablename__ = "recommendation_runs"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(String(64), unique=True, index=True, nullable=False)
    questionnaire_id = Column(Integer, ForeignKey("questionnaire_responses.id", ondelete="SET NULL"), nullable=True)
    analytical_mode = Column(String(64), default="hybrid") # hybrid, logistic_regression, factor_analysis, clustering
    model_version_id = Column(Integer, ForeignKey("model_versions.id"), nullable=True)
    total_schools_evaluated = Column(Integer, default=0)
    eligible_schools_count = Column(Integer, default=0)
    execution_time_ms = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    questionnaire = relationship("QuestionnaireResponse", back_populates="runs")
    results = relationship("RecommendationResult", back_populates="run", cascade="all, delete-orphan")


# 11. recommendation_results
class RecommendationResult(Base):
    __tablename__ = "recommendation_results"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("recommendation_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    school_id = Column(Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False, index=True)
    rank = Column(Integer, nullable=False)
    overall_match_score = Column(Float, nullable=False) # 0 to 100
    regulatory_eligibility = Column(String(32), default="verified_eligible") # verified_eligible, eligibility_uncertain, not_eligible
    cost_score = Column(Float, default=0.0)
    ranking_score = Column(Float, default=0.0)
    fleet_score = Column(Float, default=0.0)
    location_score = Column(Float, default=0.0)
    facilities_score = Column(Float, default=0.0)
    statistical_boost = Column(Float, default=0.0)
    match_reasons_json = Column(Text, nullable=True)
    tradeoffs_json = Column(Text, nullable=True)
    missing_info_json = Column(Text, nullable=True)
    budget_gap_inr = Column(Float, default=0.0)

    run = relationship("RecommendationRun", back_populates="results")
    school = relationship("School", back_populates="recommendation_results")


# 12. model_versions
class ModelVersion(Base):
    __tablename__ = "model_versions"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String(64), nullable=False, index=True) # logistic_regression, factor_analysis, kmeans_clustering
    version_tag = Column(String(32), nullable=False)
    is_active = Column(Boolean, default=True)
    is_synthetic_demonstration = Column(Boolean, default=False)
    description = Column(Text, nullable=True)
    parameters_json = Column(Text, nullable=True)
    training_sample_size = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    evaluation_runs = relationship("EvaluationRun", back_populates="model_version")


# 13. evaluation_runs
class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    id = Column(Integer, primary_key=True, index=True)
    model_version_id = Column(Integer, ForeignKey("model_versions.id"), nullable=False)
    run_timestamp = Column(DateTime, default=datetime.utcnow)
    dataset_type = Column(String(32), default="authentic") # authentic, synthetic_isolated
    sample_size = Column(Integer, nullable=False)
    metrics_json = Column(Text, nullable=False) # JSON dictionary of metrics
    status = Column(String(32), default="completed")
    notes = Column(Text, nullable=True)

    model_version = relationship("ModelVersion", back_populates="evaluation_runs")
    metrics = relationship("ModelMetric", back_populates="evaluation_run", cascade="all, delete-orphan")


# 14. model_metrics
class ModelMetric(Base):
    __tablename__ = "model_metrics"

    id = Column(Integer, primary_key=True, index=True)
    evaluation_run_id = Column(Integer, ForeignKey("evaluation_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    metric_name = Column(String(64), nullable=False, index=True) # accuracy, precision, recall, f1, roc_auc, brier_score, silhouette, inertia, kmo, ndcg_5
    metric_value = Column(Float, nullable=False)
    metric_category = Column(String(32), default="performance") # performance, diagnostic, quality
    is_statistically_significant = Column(Boolean, default=True)

    evaluation_run = relationship("EvaluationRun", back_populates="metrics")


# 15. user_feedback
class UserFeedback(Base):
    __tablename__ = "user_feedback"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(64), index=True, nullable=True)
    run_id = Column(String(64), index=True, nullable=True)
    school_id = Column(String(64), index=True, nullable=True)
    rating = Column(Integer, nullable=False) # 1 to 5
    was_helpful = Column(Boolean, default=True)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
