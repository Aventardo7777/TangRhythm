from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.rag.retriever import retrieve
from app.rag.llm import generate_answer
from app.schemas.poetry import AskRequest, AskResponse, Citation

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/ask", response_model=AskResponse)
async def ask(payload: AskRequest, db: AsyncSession = Depends(get_db)):
    hits = await retrieve(db, payload.question, payload.poem_id)
    context = "\n\n---\n\n".join(h.content for h in hits)
    answer, retrieval_mode = await generate_answer(payload.question, payload.learner_stage, context, payload.mode)
    citations = [Citation(title=h.title,source=h.source,poem_id=h.poem_id,chunk_type=h.chunk_type) for h in hits]
    return AskResponse(answer=answer,citations=citations,mode=payload.mode,retrieval_mode=retrieval_mode)
