from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.core.config import settings
from app.db.session import engine, Base
from app.models import Author, Poem, KnowledgeChunk, LearningRecord
from app.api.poems import router as poems_router
from app.api.ai import router as ai_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title=settings.app_name, version="0.2.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=[x.strip() for x in settings.cors_origins.split(',')], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(poems_router, prefix="/api")
app.include_router(ai_router, prefix="/api")

@app.get("/health")
async def health(): return {"status":"ok","service":"tangrhythm-api","version":"0.2.0"}
