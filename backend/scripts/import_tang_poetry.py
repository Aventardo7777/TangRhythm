"""Import the public-domain anthology source into PostgreSQL.

Source A: rime-aca/corpus 唐詩三百首.txt
The importer normalizes Traditional Chinese source metadata without inventing
translations or analysis. Education-layer fields are intentionally left null
until separately verified.
"""
import asyncio, hashlib, re, sys
from pathlib import Path
import httpx
from sqlalchemy import select
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.core.config import settings
from app.db.session import SessionLocal, engine, Base
from app.models import Author, Poem

async def download_source() -> str:
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.get(settings.source_url)
        r.raise_for_status()
        return r.content.decode("utf-8-sig", errors="replace")

from app.data.normalizer import parse_records, stable_id

async def main():
    text=await download_source()
    records=parse_records(text)
    if not (280 <= len(records) <= 340):
        raise RuntimeError(f"Unexpected source record count: {len(records)}")
    source_hash=hashlib.sha256(text.encode()).hexdigest()
    async with engine.begin() as conn: await conn.run_sync(Base.metadata.create_all)
    async with SessionLocal() as db:
        for rec in records:
            author=(await db.scalars(select(Author).where(Author.name==rec["author"]))).first()
            if not author:
                author=Author(name=rec["author"],period="唐",source=settings.source_url)
                db.add(author); await db.flush()
            poem_id=stable_id(rec["title"], rec["author"], rec["anthology_index"])
            poem=await db.get(Poem,poem_id)
            if not poem:
                poem=Poem(id=poem_id,anthology_index=rec["anthology_index"],title=rec["title"],author_id=author.id,dynasty="唐",genre=rec["genre"],content=rec["content"],source_url=settings.source_url,source_name="rime-aca/corpus · 唐詩三百首.txt",source_hash=source_hash)
                db.add(poem)
            else:
                poem.title=rec["title"]; poem.content=rec["content"]; poem.source_hash=source_hash
        await db.commit()
    print(f"Imported {len(records)} records. SHA256={source_hash}")

if __name__ == "__main__": asyncio.run(main())
