from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "SkyMatch India - Intelligent Flying School Recommendation System"
    API_V1_STR: str = "/api"
    SECRET_KEY: str = "skymatch-india-development-secret-key-2026"
    ADMIN_API_KEY: str = "admin-secret-dgca-2026"
    
    # Database: SQLite fallback for local dev or PostgreSQL
    DATABASE_URL: str = "sqlite:///./skymatch.db"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://localhost:8000"
    ]
    
    # Data Paths
    DATA_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "data")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
