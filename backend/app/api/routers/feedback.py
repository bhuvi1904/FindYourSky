from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
from app.db.session import get_db
from app.models.entities import UserFeedback

router = APIRouter(prefix="/feedback", tags=["User Feedback"])

class FeedbackSubmission(BaseModel):
    session_id: Optional[str] = None
    run_id: Optional[str] = None
    school_id: Optional[str] = None
    rating: int = Field(..., ge=1, le=5)
    was_helpful: bool = True
    comments: Optional[str] = None

@router.post("")
def submit_feedback(data: FeedbackSubmission, db: Session = Depends(get_db)):
    """
    Submits user feedback regarding recommendation accuracy, transparency, and UI usefulness.
    """
    fb = UserFeedback(
        session_id=data.session_id,
        run_id=data.run_id,
        school_id=data.school_id,
        rating=data.rating,
        was_helpful=data.was_helpful,
        comments=data.comments
    )
    db.add(fb)
    db.commit()
    return {"status": "success", "message": "Thank you for your feedback! Your submission helps refine recommendation relevance."}
