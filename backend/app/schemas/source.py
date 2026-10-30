from pydantic import BaseModel
from typing import List, Optional

class DataSourceSchema(BaseModel):
    id: Optional[int] = None
    source_id: str
    name: str
    url: str
    source_type: str
    publisher: Optional[str] = None
    description: Optional[str] = None
    verification_status: str
    retrieval_date: Optional[str] = None

    class Config:
        from_attributes = True

class SourceObservationSchema(BaseModel):
    id: Optional[int] = None
    school_id: int
    source_id: int
    field_name: str
    observed_value: Optional[str] = None
    verification_status: str
    confidence_level: float
    observation_date: Optional[str] = None
    retrieval_date: Optional[str] = None
    source_url: Optional[str] = None

    class Config:
        from_attributes = True
