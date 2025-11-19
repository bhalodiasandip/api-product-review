from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN") # optional if you want to verify
    TWILIO_AUTH_SID: str = os.getenv("TWILIO_AUTH_SID")

class Config:
    env_file = ".env"

settings = Settings()