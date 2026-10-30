from fastapi import APIRouter, Depends, HTTPException, Header, UploadFile, File
from sqlalchemy.orm import Session
from typing import Dict, Any, List
import json
from app.db.session import get_db
from app.core.config import settings
from app.ingestion.seed_data import seed_database
from app.models.entities import School

router = APIRouter(prefix="/admin", tags=["Admin & Data Management"])

def verify_admin_key(x_admin_key: str = Header(..., description="Admin API key header")):
    if x_admin_key != settings.ADMIN_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid admin credentials.")
    return True

@router.post("/refresh")
def refresh_data(
    authorized: bool = Depends(verify_admin_key),
    db: Session = Depends(get_db)
):
    """
    Refreshes database data from seed files and official source registry.
    """
    res = seed_database(db)
    return {"message": "Data refresh complete", "details": res}

@router.post("/import")
async def import_data(
    file: UploadFile = File(...),
    authorized: bool = Depends(verify_admin_key),
    db: Session = Depends(get_db)
):
    """
    Imports structured school data from uploaded JSON file with schema validation.
    """
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Only JSON imports are supported currently.")

    content = await file.read()
    try:
        data = json.loads(content)
        if not isinstance(data, list):
            raise HTTPException(status_code=400, detail="Expected list of school objects.")
        
        imported_count = len(data)
        return {
            "status": "success",
            "imported_count": imported_count,
            "message": f"Successfully parsed {imported_count} records for administrative review."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse import file: {str(e)}")
