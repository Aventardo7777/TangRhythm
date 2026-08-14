import asyncio
from app.main import app

if __name__ == "__main__":
    print("Database initialization is performed by FastAPI lifespan.")
    print("Run: uvicorn app.main:app --reload")
