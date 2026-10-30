from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.entities import DataSource
from app.schemas.source import DataSourceSchema

router = APIRouter(prefix="/sources", tags=["Sources & Provenance"])

@router.get("", response_model=List[DataSourceSchema])
def list_sources(db: Session = Depends(get_db)):
    """
    Returns the authoritative source registry including DGCA, MoCA, and PIB publications.
    """
    return db.query(DataSource).all()

@router.get("/{source_id}", response_model=DataSourceSchema)
def get_source(source_id: str, db: Session = Depends(get_db)):
    source = db.query(DataSource).filter(DataSource.source_id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail=f"Source '{source_id}' not found.")
    return source
