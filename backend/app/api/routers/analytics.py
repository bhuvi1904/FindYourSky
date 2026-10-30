from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.entities import School
from app.schemas.analytics import (
    AnalyticsOverviewResponse, LogisticRegressionSummary,
    FactorAnalysisSummary, ClusteringSummary
)
from app.analytics.logistic_regression import train_and_evaluate_logistic_regression
from app.analytics.factor_analysis import run_factor_analysis
from app.analytics.clustering import run_kmeans_clustering

router = APIRouter(prefix="/analytics", tags=["Statistical Analytics & Modeling"])

@router.get("/overview", response_model=AnalyticsOverviewResponse)
def get_analytics_overview(db: Session = Depends(get_db)):
    """
    Returns high-level business analytics, active statistical models status, and dataset summary.
    """
    schools = db.query(School).all()
    total = len(schools)
    verified = sum(1 for s in schools if s.confidence_score >= 0.90)
    avg_completeness = sum(s.completeness_score for s in schools) / max(1, total)

    return AnalyticsOverviewResponse(
        total_schools=total,
        verified_schools_count=verified,
        active_models_count=3,
        logistic_regression_ready=(total >= 8),
        factor_analysis_ready=(total >= 6),
        clustering_ready=(total >= 4),
        data_completeness_average=round(float(avg_completeness) * 100.0, 1)
    )

@router.get("/logistic-regression", response_model=LogisticRegressionSummary)
def get_logistic_regression_model(
    synthetic_demo: bool = Query(False, description="Run on isolated synthetic demonstration dataset"),
    db: Session = Depends(get_db)
):
    """
    Returns computational Scikit-learn Logistic Regression coefficients, odds ratios,
    probabilities, ROC curve coordinates, and cross-validation performance.
    """
    schools = db.query(School).all()
    result = train_and_evaluate_logistic_regression(schools, use_synthetic_benchmark=synthetic_demo)
    return LogisticRegressionSummary(**result)

@router.get("/factor-analysis", response_model=FactorAnalysisSummary)
def get_factor_analysis_model(
    factors: int = Query(3, ge=2, le=5, description="Number of latent factors to extract"),
    db: Session = Depends(get_db)
):
    """
    Returns Exploratory Factor Analysis with KMO sample adequacy, Bartlett sphericity test,
    Scree plot eigenvalues, Varimax loadings, and school factor scores.
    """
    schools = db.query(School).all()
    result = run_factor_analysis(schools, n_factors=factors)
    return FactorAnalysisSummary(**result)

@router.get("/clustering", response_model=ClusteringSummary)
def get_clustering_model(
    k: int = Query(None, description="Optional fixed cluster count K (default auto-selects optimal K)"),
    db: Session = Depends(get_db)
):
    """
    Returns K-Means clustering with inertia elbow curve, silhouette score,
    data-driven cluster centroids, 2D PCA projection coordinates, and stability index.
    """
    schools = db.query(School).all()
    result = run_kmeans_clustering(schools, fixed_k=k)
    return ClusteringSummary(**result)
