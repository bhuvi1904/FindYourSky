from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class SchoolBaseSchema(BaseModel):
    id: Optional[int] = None
    base_id: str
    is_primary: bool = False
    airport_name: str
    icao_code: Optional[str] = None
    city: str
    state: str
    region: str
    runway_length_meters: Optional[int] = None
    runway_surface: Optional[str] = None
    night_flying_available: bool = False
    atc_type: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    class Config:
        from_attributes = True

class AircraftFleetSchema(BaseModel):
    id: Optional[int] = None
    aircraft_model: str
    manufacturer: Optional[str] = None
    engine_type: str
    avionics_type: Optional[str] = None
    count: int = 1
    operational_count: int = 1
    fuel_type: Optional[str] = None

    class Config:
        from_attributes = True

class SchoolFeeSchema(BaseModel):
    id: Optional[int] = None
    course_name: str
    currency: str = "INR"
    tuition_flying_inr: float
    ground_school_inr: float = 0.0
    simulator_inr: float = 0.0
    hostel_mess_annual_inr: float = 0.0
    tax_gst_inr: float = 0.0
    total_estimated_inr: float
    is_fee_inclusive_hostel: bool = False
    is_fee_verified: bool = False
    fee_effective_date: Optional[str] = None
    source_url: Optional[str] = None
    inclusions: List[str] = []
    exclusions: List[str] = []
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class DGCARankingSchema(BaseModel):
    id: Optional[int] = None
    ranking_period: str
    ranking_category: str
    overall_score: Optional[float] = None
    national_rank: Optional[int] = None
    annual_hours_logged: Optional[float] = None
    safety_audit_score: Optional[float] = None
    cfi_cadre_strength: Optional[int] = None
    source_id: Optional[str] = None
    effective_date: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class SchoolProgrammeSchema(BaseModel):
    id: Optional[int] = None
    programme_name: str
    licence_type: str = "CPL"
    duration_months: int = 15
    description: Optional[str] = None

    class Config:
        from_attributes = True

class SchoolDetailSchema(BaseModel):
    id: int
    school_id: str
    name: str
    short_name: Optional[str] = None
    slug: str
    website_url: str
    ownership_type: str
    dgca_approval_no: str
    approval_validity: Optional[str] = None
    operational_status: str
    established_year: Optional[int] = None
    confidence_score: float
    completeness_score: float
    last_verified_date: Optional[str] = None
    is_synthetic: bool = False
    bases: List[SchoolBaseSchema] = []
    fleet: List[AircraftFleetSchema] = []
    fees: List[SchoolFeeSchema] = []
    rankings: List[DGCARankingSchema] = []
    programmes: List[SchoolProgrammeSchema] = []

    class Config:
        from_attributes = True

class SchoolSummarySchema(BaseModel):
    id: int
    school_id: str
    name: str
    short_name: Optional[str] = None
    slug: str
    website_url: str
    ownership_type: str
    dgca_approval_no: str
    operational_status: str
    latest_ranking_category: Optional[str] = "Unranked"
    latest_dgca_score: Optional[float] = None
    primary_city: Optional[str] = None
    primary_state: Optional[str] = None
    primary_region: Optional[str] = None
    total_fleet_count: int = 0
    multi_engine_count: int = 0
    glass_cockpit_available: bool = False
    night_flying_available: bool = False
    indicative_fee_inr: Optional[float] = None
    is_fee_verified: bool = False
    confidence_score: float = 1.0
    completeness_score: float = 1.0
    is_synthetic: bool = False

    class Config:
        from_attributes = True
