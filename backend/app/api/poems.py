from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models import Poem, Author
from app.schemas.poetry import PoemOut, PoemSummary, SearchResult

router = APIRouter(prefix="/poems", tags=["poetry"])

def to_summary(p: Poem) -> PoemSummary:
    return PoemSummary(id=p.id,title=p.title,author=p.author.name if p.author else None,dynasty=p.dynasty,period=p.period,genre=p.genre,theme=p.theme or [],emotion=p.emotion or [],content=p.content)

def to_out(p: Poem) -> PoemOut:
    return PoemOut(**to_summary(p).model_dump(), translation=p.translation, annotation=p.annotation, background=p.background, appreciation=p.appreciation, imagery=p.imagery or [], literary_devices=p.literary_devices or [], famous_lines=p.famous_lines or [], keywords=p.keywords or [], difficulty=p.difficulty, source_url=p.source_url, source_name=p.source_name, author_detail=p.author)

@router.get("", response_model=list[PoemSummary])
async def list_poems(db: AsyncSession = Depends(get_db), limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)):
    q = select(Poem).order_by(Poem.anthology_index.nulls_last(), Poem.title).offset(offset).limit(limit)
    return [to_summary(x) for x in (await db.scalars(q)).all()]

@router.get("/search", response_model=SearchResult)
async def search_poems(q: str = Query(min_length=1, max_length=100), db: AsyncSession = Depends(get_db), limit: int = Query(20, ge=1, le=100)):
    pattern = f"%{q}%"
    stmt = select(Poem).outerjoin(Author).where(or_(Poem.title.ilike(pattern), Poem.content.ilike(pattern), Author.name.ilike(pattern))).limit(limit)
    rows = [to_summary(x) for x in (await db.scalars(stmt)).all()]
    total = await db.scalar(select(func.count()).select_from(Poem).outerjoin(Author).where(or_(Poem.title.ilike(pattern), Poem.content.ilike(pattern), Author.name.ilike(pattern)))) or 0
    return SearchResult(results=rows,total=total)

@router.get("/{poem_id}", response_model=PoemOut)
async def get_poem(poem_id: str, db: AsyncSession = Depends(get_db)):
    p = await db.get(Poem, poem_id)
    if not p: raise HTTPException(404, "Poem not found")
    return to_out(p)
