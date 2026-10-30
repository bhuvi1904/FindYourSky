from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.session import get_db
from app.models.entities import School, SourceObservation
from app.schemas.school import SchoolSummarySchema, SchoolDetailSchema
from app.schemas.source import SourceObservationSchema

router = APIRouter(prefix="/schools", tags=["Schools"])

@router.get("", response_model=List[SchoolSummarySchema])
def list_schools(
    region: Optional[str] = Query(None, description="Filter by geographical region (North, South, East, West, Central)"),
    state: Optional[str] = Query(None, description="Filter by state"),
    ranking_category: Optional[str] = Query(None, description="Filter by DGCA ranking category"),
    ownership_type: Optional[str] = Query(None, description="Filter by ownership type"),
    has_multi_engine: Optional[bool] = Query(None, description="Require multi-engine fleet"),
    max_budget: Optional[float] = Query(None, description="Max tuition budget in INR"),
    search: Optional[str] = Query(None, description="Search by name, city, or airport"),
    db: Session = Depends(get_db)
):
    query = db.query(School)
    schools = query.all()

    results = []
    for s in schools:
        base = next((b for b in s.bases if b.is_primary), s.bases[0] if s.bases else None)
        fee = s.fees[0] if s.fees else None
        ranking = s.rankings[0] if s.rankings else None

        total_fleet = sum(fl.operational_count for fl in s.fleet)
        me_count = sum(fl.operational_count for fl in s.fleet if fl.engine_type == "multi_engine")
        glass = any(fl.avionics_type and "Glass" in fl.avionics_type for fl in s.fleet)
        night = base.night_flying_available if base else False

        # Apply Filters
        if region and base and base.region.lower() != region.lower():
            continue
        if state and base and base.state.lower() != state.lower():
            continue
        if ranking_category and ranking and ranking.ranking_category != ranking_category:
            continue
        if ownership_type and s.ownership_type != ownership_type:
            continue
        if has_multi_engine and me_count == 0:
            continue
        if max_budget and fee and fee.total_estimated_inr > max_budget:
            continue
        if search:
            q = search.lower()
            name_match = q in s.name.lower() or (s.short_name and q in s.short_name.lower())
            city_match = base and (q in base.city.lower() or q in base.airport_name.lower() or (base.icao_code and q in base.icao_code.lower()))
            if not (name_match or city_match):
                continue

        results.append(SchoolSummarySchema(
            id=s.id,
            school_id=s.school_id,
            name=s.name,
            short_name=s.short_name,
            slug=s.slug,
            website_url=s.website_url,
            ownership_type=s.ownership_type,
            dgca_approval_no=s.dgca_approval_no,
            operational_status=s.operational_status,
            latest_ranking_category=ranking.ranking_category if ranking else "Unranked",
            latest_dgca_score=ranking.overall_score if ranking else None,
            primary_city=base.city if base else None,
            primary_state=base.state if base else None,
            primary_region=base.region if base else None,
            total_fleet_count=total_fleet,
            multi_engine_count=me_count,
            glass_cockpit_available=glass,
            night_flying_available=night,
            indicative_fee_inr=fee.total_estimated_inr if fee else None,
            is_fee_verified=fee.is_fee_verified if fee else False,
            confidence_score=s.confidence_score,
            completeness_score=s.completeness_score,
            is_synthetic=s.is_synthetic
        ))

    return results

@router.get("/{school_id}", response_model=SchoolDetailSchema)
def get_school_detail(school_id: str, db: Session = Depends(get_db)):
    school = db.query(School).filter(
        (School.school_id == school_id) | (School.slug == school_id)
    ).first()
    if not school:
        raise HTTPException(status_code=404, detail=f"School '{school_id}' not found.")
    return school

@router.get("/{school_id}/sources", response_model=List[SourceObservationSchema])
def get_school_sources(school_id: str, db: Session = Depends(get_db)):
    school = db.query(School).filter(
        (School.school_id == school_id) | (School.slug == school_id)
    ).first()
    if not school:
        raise HTTPException(status_code=404, detail=f"School '{school_id}' not found.")
    return db.query(SourceObservation).filter(SourceObservation.school_id == school.id).all()
