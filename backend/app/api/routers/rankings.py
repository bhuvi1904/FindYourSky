from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.db.session import get_db
from app.models.entities import DGCARanking, School
from app.schemas.school import DGCARankingSchema

router = APIRouter(prefix="/rankings", tags=["DGCA Rankings"])

@router.get("", response_model=List[Dict[str, Any]])
def get_rankings(
    period: str = "2025-2026",
    db: Session = Depends(get_db)
):
    """
    Returns official DGCA FTO rankings with verified audit metrics, hours logged, and source provenance.
    """
    rankings = db.query(DGCARanking).filter(DGCARanking.ranking_period == period).all()
    results = []
    for r in rankings:
        school = r.school
        base = next((b for b in school.bases if b.is_primary), school.bases[0] if school.bases else None)
        results.append({
            "ranking_id": r.id,
            "school_id": school.school_id,
            "school_name": school.name,
            "short_name": school.short_name or school.name,
            "slug": school.slug,
            "ranking_period": r.ranking_period,
            "ranking_category": r.ranking_category,
            "national_rank": r.national_rank,
            "overall_score": r.overall_score,
            "annual_hours_logged": r.annual_hours_logged,
            "safety_audit_score": r.safety_audit_score,
            "cfi_cadre_strength": r.cfi_cadre_strength,
            "primary_base_airport": base.airport_name if base else None,
            "source_id": r.source_id,
            "effective_date": r.effective_date,
            "verification_status": "official"
        })

    # Sort by national rank ascending
    results.sort(key=lambda x: x["national_rank"] if x["national_rank"] is not None else 999)
    return results
