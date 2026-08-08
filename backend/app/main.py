from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "AI Personal Finance Assistant API is running!"
    }


@app.get("/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "not connected",
            "error": str(e)
        }