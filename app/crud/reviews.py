from sqlalchemy.orm import Session
from typing import List
from app.models import review
from app.schemas.review import ReviewCreate
from datetime import datetime


def create_review(db: Session, review_in: ReviewCreate):
    db_review = review.Review(
        contact_number=review_in.contact_number,
        user_name=review_in.user_name,
        product_name=review_in.product_name,
        product_review=review_in.product_review,
        created_at=datetime.now()
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews(db: Session, skip: int = 0, limit: int = 100) -> List[review.Review]:
    return db.query(review.Review).order_by(review.Review.created_at.desc()).offset(skip).limit(limit).all()