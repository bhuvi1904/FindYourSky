from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.init_db import init_db
from app.api.routers import (
    schools, rankings, sources, questionnaire,
    recommendations, analytics, evaluation, admin, feedback
)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Statistical recommendation and business analytics system for DGCA-approved Indian Flying Training Organisations.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup Event: Initialize Schema & Seed Data
@app.on_event("startup")
def on_startup():
    init_db()

# Health Endpoint
@app.get("/api/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "FindYourSky Backend API",
        "version": "1.0.0",
        "models": {
            "logistic_regression": "ready",
            "factor_analysis": "ready",
            "kmeans_clustering": "ready",
            "hybrid_recommender": "ready"
        }
    }

# Include API Routers
app.include_router(schools.router, prefix=settings.API_V1_STR)
app.include_router(rankings.router, prefix=settings.API_V1_STR)
app.include_router(sources.router, prefix=settings.API_V1_STR)
app.include_router(questionnaire.router, prefix=settings.API_V1_STR)
app.include_router(recommendations.router, prefix=settings.API_V1_STR)
app.include_router(analytics.router, prefix=settings.API_V1_STR)
app.include_router(evaluation.router, prefix=settings.API_V1_STR)
app.include_router(admin.router, prefix=settings.API_V1_STR)
app.include_router(feedback.router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
