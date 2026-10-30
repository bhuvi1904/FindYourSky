from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from datetime import datetime

class MetricEntry(BaseModel):
    metric_name: str
    metric_value: float
    category: str
    is_statistically_significant: bool = True

class ModelEvaluationReport(BaseModel):
    model_name: str
    version_tag: str
    is_synthetic_demonstration: bool
    dataset_type: str # authentic, synthetic_isolated
    sample_size: int
    positive_labels: Optional[int] = None
    negative_labels: Optional[int] = None
    metrics: Dict[str, float]
    diagnostics: Dict[str, Any]
    evaluation_timestamp: str

class RecommendationQualityReport(BaseModel):
    benchmark_dataset: str
    total_queries_evaluated: int
    ndcg_at_3: float
    ndcg_at_5: float
    precision_at_3: float
    precision_at_5: float
    recall_at_5: float
    mrr: float
    baseline_ndcg_at_5: float # vs naive popularity or random
    relevance_methodology: str

class DataQualityDashboard(BaseModel):
    total_schools: int
    verified_approval_pct: float
    verified_website_pct: float
    verified_ranking_pct: float
    published_fee_pct: float
    missingness_by_field: Dict[str, float]
    stale_records_count: int
    source_coverage_count: int
    last_refresh_date: str
    completeness_distribution: Dict[str, int]
