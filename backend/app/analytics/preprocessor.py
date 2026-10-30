import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple
from app.models.entities import School

FEATURE_COLUMNS = [
    "tuition_fee_lakhs",
    "total_fleet",
    "multi_engine_fleet",
    "dgca_score",
    "annual_flying_hours_k",
    "safety_audit_score",
    "cfi_cadre",
    "night_flying",
    "runway_length_km",
    "controlled_airspace",
    "completeness_score"
]

def extract_school_features(schools: List[School]) -> Tuple[pd.DataFrame, List[Dict[str, Any]]]:
    """
    Transforms relational school entities into a standardized pandas DataFrame for ML/analytics.
    Handles missing values transparently without imputing fee as 0.
    """
    records = []
    metadata = []

    for s in schools:
        fee_obj = s.fees[0] if s.fees else None
        rank_obj = s.rankings[0] if s.rankings else None
        base = next((b for b in s.bases if b.is_primary), s.bases[0] if s.bases else None)

        total_fleet = sum(fl.operational_count for fl in s.fleet)
        me_fleet = sum(fl.operational_count for fl in s.fleet if fl.engine_type == "multi_engine")

        # Fee in Lakhs (INR / 100,000)
        fee_lakhs = (fee_obj.total_estimated_inr / 100000.0) if (fee_obj and fee_obj.total_estimated_inr > 0) else np.nan

        # DGCA score
        dgca_score = rank_obj.overall_score if (rank_obj and rank_obj.overall_score is not None) else np.nan
        annual_hours = (rank_obj.annual_hours_logged / 1000.0) if (rank_obj and rank_obj.annual_hours_logged is not None) else np.nan
        safety_audit = rank_obj.safety_audit_score if (rank_obj and rank_obj.safety_audit_score is not None) else np.nan
        cfi_cadre = rank_obj.cfi_cadre_strength if (rank_obj and rank_obj.cfi_cadre_strength is not None) else np.nan

        night_flying = 1.0 if (base and base.night_flying_available) else 0.0
        runway_km = (base.runway_length_meters / 1000.0) if (base and base.runway_length_meters) else 1.2
        controlled_airspace = 1.0 if (base and base.atc_type and ("Controlled" in base.atc_type or "Tower" in base.atc_type)) else 0.0

        records.append({
            "school_id": s.school_id,
            "name": s.name,
            "tuition_fee_lakhs": fee_lakhs,
            "total_fleet": float(total_fleet),
            "multi_engine_fleet": float(me_fleet),
            "dgca_score": dgca_score,
            "annual_flying_hours_k": annual_hours,
            "safety_audit_score": safety_audit,
            "cfi_cadre": float(cfi_cadre) if not np.isnan(cfi_cadre) else np.nan,
            "night_flying": night_flying,
            "runway_length_km": runway_km,
            "controlled_airspace": controlled_airspace,
            "completeness_score": float(s.completeness_score)
        })

        metadata.append({
            "school_id": s.school_id,
            "name": s.name,
            "short_name": s.short_name or s.name,
            "slug": s.slug,
            "ownership_type": s.ownership_type,
            "ranking_category": rank_obj.ranking_category if rank_obj else "Unranked",
            "is_fee_verified": fee_obj.is_fee_verified if fee_obj else False,
            "primary_city": base.city if base else "Unknown",
            "primary_state": base.state if base else "Unknown",
            "primary_region": base.region if base else "Unknown"
        })

    df = pd.DataFrame(records)
    return df, metadata
