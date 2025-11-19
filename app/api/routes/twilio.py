from fastapi import APIRouter, Form, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.twilio_flow import handle_incoming
from app.schemas.review import ReviewCreate
from app.crud.reviews import create_review

router = APIRouter()


@router.post("/twilio/webhook")
async def twilio_webhook(
    From: str = Form(...),
    Body: str = Form(""),
    db: Session = Depends(get_db),
):
    reply, payload = handle_incoming(From, Body)

    # If payload exists → conversation completed → save review
    if payload:
        review_in = ReviewCreate(**payload)
        create_review(db, review_in)

    return PlainTextResponse(reply)
