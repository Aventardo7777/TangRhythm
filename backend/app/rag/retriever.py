from dataclasses import dataclass
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Poem, KnowledgeChunk

@dataclass
class RetrievalHit:
    title: str
    content: str
    poem_id: str | None
    source: str | None
    chunk_type: str | None
    score: float

async def retrieve(db: AsyncSession, query: str, poem_id: str | None = None, limit: int = 6) -> list[RetrievalHit]:
    tokens = [t for t in query.strip().split() if t]
    clauses = []
    for t in tokens[:12]:
        pattern = f"%{t}%"
        clauses.append(Poem.title.ilike(pattern))
        clauses.append(Poem.content.ilike(pattern))
        clauses.append(Poem.background.ilike(pattern))
        clauses.append(Poem.appreciation.ilike(pattern))
    if poem_id:
        clauses.append(Poem.id == poem_id)
    stmt = select(Poem).where(or_(*clauses)) if clauses else select(Poem)
    poems = (await db.scalars(stmt.limit(limit))).all()
    hits=[]
    for p in poems:
        score = sum(p.title.find(t) >= 0 for t in tokens) * 3 + sum(p.content.find(t) >= 0 for t in tokens)
        hits.append(RetrievalHit(p.title, p.content + "\n" + (p.background or "") + "\n" + (p.appreciation or ""), p.id, p.source_url, "poem", float(score)))
    hits.sort(key=lambda x:x.score, reverse=True)
    return hits[:limit]
