from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.review import ReviewCreate, ReviewOut
from app.crud.reviews import create_review, get_reviews

router = APIRouter()


@router.get("/reviews", response_model=list[ReviewOut])
def list_reviews(db: Session = Depends(get_db)):
    return get_reviews(db)


@router.post("/reviews", response_model=ReviewOut, status_code=201)
def add_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db, review)
