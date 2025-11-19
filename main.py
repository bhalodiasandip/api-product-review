from fastapi import FastAPI
from app.db.session import engine
from app import models
from app.api.routes import reviews, twilio
from fastapi.middleware.cors import CORSMiddleware

# create tables (for dev). In production use Alembic migrations.
models.review.Base.metadata.create_all(bind=engine)

app = FastAPI(title="WhatsApp Product Review Collector")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],          # VERY IMPORTANT for OPTIONS
    allow_headers=["*"],
)

app.include_router(reviews.router,prefix="/api")
app.include_router(twilio.router)

@app.get("/")
def root():
    return {"status": "ok"}