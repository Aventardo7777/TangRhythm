"""Optional AI enrichment pipeline.

It never overwrites source text. Generated fields are stored as a reviewable JSONL
file first. A human can inspect the file before importing enrichment into PostgreSQL.
"""
import asyncio, json, sys
from pathlib import Path
import httpx
from sqlalchemy import select
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Poem

SCHEMA = {
  "translation":"string",
  "background":"string",
  "appreciation":"string",
  "theme":["string"],
  "emotion":["string"],
  "imagery":["string"],
  "literary_devices":["string"],
  "famous_lines":["string"],
  "teaching_points":["string"],
  "exam_points":["string"]
}

async def enrich(poem: Poem):
    if not settings.llm_api_key:
        raise RuntimeError("LLM_API_KEY is required for enrichment; source text import works without it.")
    system = "你是古典诗词教学编辑。只能依据给定诗文和明确可靠背景做教育性整理。不得编造。输出严格 JSON。"
    user = f"诗题：{poem.title}\n作者：{poem.author.name if poem.author else ''}\n体裁：{poem.genre}\n诗文：{poem.content}\nJSON字段结构：{json.dumps(SCHEMA,ensure_ascii=False)}"
    payload={"model":settings.llm_model,"messages":[{"role":"system","content":system},{"role":"user","content":user}],"temperature":0.1}
    async with httpx.AsyncClient(timeout=90) as client:
        r=await client.post(settings.llm_base_url.rstrip('/')+'/chat/completions',headers={"Authorization":f"Bearer {settings.llm_api_key}"},json=payload)
        r.raise_for_status()
        content=r.json()['choices'][0]['message']['content']
    return json.loads(content)

async def main():
    out=Path('data/enrichment/poem_enrichment.review.jsonl'); out.parent.mkdir(parents=True,exist_ok=True)
    async with SessionLocal() as db:
        poems=(await db.scalars(select(Poem).order_by(Poem.anthology_index))).all()
        with out.open('w',encoding='utf-8') as f:
            for i,p in enumerate(poems,1):
                item=await enrich(p)
                row={"poem_id":p.id,"title":p.title,"author":p.author.name if p.author else None,"generated":item,"review_status":"needs_human_review"}
                f.write(json.dumps(row,ensure_ascii=False)+'\n')
                print(f"[{i}/{len(poems)}] {p.title}")
    print(f"Wrote review file: {out}")

if __name__=='__main__': asyncio.run(main())
