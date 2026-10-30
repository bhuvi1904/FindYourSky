import json
import os
from sqlalchemy.orm import Session
from app.core.config import settings
from app.models.entities import (
    School, SchoolBase, AircraftFleet, SchoolFee, DGCARanking,
    DataSource, SourceObservation, SchoolProgramme, ModelVersion
)

def seed_database(db: Session, force: bool = False):
    # Check if already seeded
    if not force and db.query(School).count() > 0:
        return {"status": "already_seeded", "schools_count": db.query(School).count()}

    if force:
        db.query(SourceObservation).delete()
        db.query(SchoolProgramme).delete()
        db.query(DGCARanking).delete()
        db.query(SchoolFee).delete()
        db.query(AircraftFleet).delete()
        db.query(SchoolBase).delete()
        db.query(School).delete()
        db.query(DataSource).delete()
        db.query(ModelVersion).delete()
        db.commit()

    # 1. Seed Data Sources
    sources_file = os.path.join(settings.DATA_DIR, "dgca_sources.json")
    sources_map = {}
    if os.path.exists(sources_file):
        with open(sources_file, "r", encoding="utf-8") as f:
            sources_data = json.load(f)
            for s_data in sources_data:
                source = DataSource(
                    source_id=s_data["source_id"],
                    name=s_data["name"],
                    url=s_data["url"],
                    source_type=s_data["source_type"],
                    publisher=s_data.get("publisher"),
                    description=s_data.get("description"),
                    verification_status=s_data.get("verification_status", "verified"),
                    retrieval_date=s_data.get("retrieval_date")
                )
                db.add(source)
                db.flush()
                sources_map[s_data["source_id"]] = source.id
        db.commit()

    # 2. Seed Schools
    schools_file = os.path.join(settings.DATA_DIR, "samples", "fto_seed_data.json")
    if not os.path.exists(schools_file):
        return {"status": "missing_seed_file", "path": schools_file}

    with open(schools_file, "r", encoding="utf-8") as f:
        schools_data = json.load(f)

    for item in schools_data:
        school = School(
            school_id=item["school_id"],
            name=item["name"],
            short_name=item.get("short_name"),
            slug=item["slug"],
            website_url=item["website_url"],
            ownership_type=item["ownership_type"],
            dgca_approval_no=item["dgca_approval_no"],
            approval_validity=item.get("approval_validity"),
            operational_status=item.get("operational_status", "active"),
            established_year=item.get("established_year"),
            confidence_score=item.get("confidence_score", 1.0),
            completeness_score=item.get("completeness_score", 1.0),
            last_verified_date=item.get("last_verified_date"),
            is_synthetic=item.get("is_synthetic", False)
        )
        db.add(school)
        db.flush()

        # Bases
        for b in item.get("bases", []):
            base = SchoolBase(
                school_id=school.id,
                base_id=b["base_id"],
                is_primary=b.get("is_primary", False),
                airport_name=b["airport_name"],
                icao_code=b.get("icao_code"),
                city=b["city"],
                state=b["state"],
                region=b["region"],
                runway_length_meters=b.get("runway_length_meters"),
                runway_surface=b.get("runway_surface"),
                night_flying_available=b.get("night_flying_available", False),
                atc_type=b.get("atc_type"),
                latitude=b.get("latitude"),
                longitude=b.get("longitude")
            )
            db.add(base)

        # Fleet
        for fl in item.get("fleet", []):
            fleet_item = AircraftFleet(
                school_id=school.id,
                aircraft_model=fl["aircraft_model"],
                manufacturer=fl.get("manufacturer"),
                engine_type=fl["engine_type"],
                avionics_type=fl.get("avionics_type"),
                count=fl.get("count", 1),
                operational_count=fl.get("operational_count", 1),
                fuel_type=fl.get("fuel_type")
            )
            db.add(fleet_item)

        # Fees
        fee_data = item.get("fees")
        if fee_data:
            fee = SchoolFee(
                school_id=school.id,
                course_name=fee_data.get("course_name", "CPL Standard Course"),
                currency=fee_data.get("currency", "INR"),
                tuition_flying_inr=fee_data.get("tuition_flying_inr", 0.0),
                ground_school_inr=fee_data.get("ground_school_inr", 0.0),
                simulator_inr=fee_data.get("simulator_inr", 0.0),
                hostel_mess_annual_inr=fee_data.get("hostel_mess_annual_inr", 0.0),
                tax_gst_inr=fee_data.get("tax_gst_inr", 0.0),
                total_estimated_inr=fee_data.get("total_estimated_inr", 0.0),
                is_fee_inclusive_hostel=fee_data.get("is_fee_inclusive_hostel", False),
                is_fee_verified=fee_data.get("is_fee_verified", False),
                fee_effective_date=fee_data.get("fee_effective_date"),
                source_url=fee_data.get("source_url"),
                inclusions_json=json.dumps(fee_data.get("inclusions", [])),
                exclusions_json=json.dumps(fee_data.get("exclusions", [])),
            )
            db.add(fee)

        # Rankings
        rk_data = item.get("ranking")
        if rk_data:
            ranking = DGCARanking(
                school_id=school.id,
                ranking_period=rk_data.get("ranking_period", "2025-2026"),
                ranking_category=rk_data.get("ranking_category", "Unranked"),
                overall_score=rk_data.get("overall_score"),
                national_rank=rk_data.get("national_rank"),
                annual_hours_logged=rk_data.get("annual_hours_logged"),
                safety_audit_score=rk_data.get("safety_audit_score"),
                cfi_cadre_strength=rk_data.get("cfi_cadre_strength"),
                source_id=rk_data.get("source_id", "SRC_PIB_FTO_2026"),
                effective_date="2026-04-01"
            )
            db.add(ranking)

        # Programmes
        for prog_name in item.get("programmes", []):
            programme = SchoolProgramme(
                school_id=school.id,
                programme_name=prog_name,
                licence_type="CPL" if "CPL" in prog_name else "Other",
                duration_months=item.get("training_capacity", {}).get("avg_completion_months", 16)
            )
            db.add(programme)

        # Provenance Observation
        default_source_db_id = sources_map.get("SRC_DGCA_PORTAL")
        if default_source_db_id:
            obs = SourceObservation(
                school_id=school.id,
                source_id=default_source_db_id,
                field_name="dgca_approval_no",
                observed_value=item["dgca_approval_no"],
                verification_status="official",
                confidence_level=item.get("confidence_score", 1.0),
                observation_date=item.get("last_verified_date", "2026-10-15"),
                retrieval_date="2026-10-26",
                source_url="https://www.dgca.gov.in/"
            )
            db.add(obs)

    db.commit()

    # 3. Seed Default Model Versions
    m_lr = ModelVersion(
        model_name="logistic_regression",
        version_tag="v1.0-authentic-baseline",
        is_active=True,
        is_synthetic_demonstration=False,
        description="Scikit-Learn Logistic Regression model with grouped cross-validation for student suitability prediction.",
        training_sample_size=db.query(School).count()
    )
    m_fa = ModelVersion(
        model_name="factor_analysis",
        version_tag="v1.0-efa-varimax",
        is_active=True,
        is_synthetic_demonstration=False,
        description="Exploratory Factor Analysis with Varimax rotation, extracting latent dimensions of Affordability, Operational Scale, and Fleet Modernness.",
        training_sample_size=db.query(School).count()
    )
    m_km = ModelVersion(
        model_name="kmeans_clustering",
        version_tag="v1.0-kmeans-k3",
        is_active=True,
        is_synthetic_demonstration=False,
        description="K-Means Clustering on standardized operational features with inertia and silhouette diagnostics.",
        training_sample_size=db.query(School).count()
    )
    db.add_all([m_lr, m_fa, m_km])
    db.commit()

    return {"status": "success", "seeded_schools": db.query(School).count()}
