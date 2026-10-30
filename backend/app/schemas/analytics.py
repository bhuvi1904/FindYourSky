from pydantic import BaseModel
from typing import List, Dict, Optional, Any

# Logistic Regression Schemas
class LogisticRegressionSummary(BaseModel):
    is_available: bool
    status_message: str
    sample_size: int
    positive_count: int
    negative_count: int
    features: List[str]
    coefficients: Dict[str, float]
    odds_ratios: Dict[str, float]
    intercept: float
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    roc_auc: Optional[float] = None
    brier_score: Optional[float] = None
    confusion_matrix: Optional[List[List[int]]] = None
    roc_curve_points: Optional[List[Dict[str, float]]] = None
    is_synthetic_demonstration: bool = False
    validation_method: str = "Stratified K-Fold Grouped CV"
    training_timestamp: Optional[str] = None

# Factor Analysis Schemas
class FactorAnalysisSummary(BaseModel):
    is_available: bool
    status_message: str
    sample_size: int
    feature_count: int
    features: List[str]
    kmo_overall: Optional[float] = None
    kmo_per_variable: Optional[Dict[str, float]] = None
    bartlett_chi_square: Optional[float] = None
    bartlett_p_value: Optional[float] = None
    num_factors_selected: int
    eigenvalues: List[float]
    cumulative_variance: List[float]
    factor_loadings: Dict[str, List[float]] # feature -> [loading_F1, loading_F2, ...]
    communalities: Dict[str, float]
    factor_labels: List[str]
    school_factor_scores: List[Dict[str, Any]] = []

# K-means Clustering Schemas
class ClusteringSummary(BaseModel):
    is_available: bool
    status_message: str
    optimal_k: int
    candidate_k_values: List[int]
    inertias: List[float]
    silhouette_scores: List[float]
    cluster_profiles: List[Dict[str, Any]]
    school_cluster_assignments: List[Dict[str, Any]]
    pca_2d_points: List[Dict[str, Any]] # school_id, name, x, y, cluster
    stability_score: float # across random seeds

# Analytics Overview
class AnalyticsOverviewResponse(BaseModel):
    total_schools: int
    verified_schools_count: int
    active_models_count: int
    logistic_regression_ready: bool
    factor_analysis_ready: bool
    clustering_ready: bool
    data_completeness_average: float
