import httpx
from app.core.config import settings
from app.rag.prompt import build_prompt

async def generate_answer(question: str, stage: str, context: str, mode: str) -> tuple[str, str]:
    prompt = build_prompt(question, stage, context, mode)
    if not settings.llm_api_key:
        # No hallucinated API result: return retrieval-grounded fallback.
        lead = "根据当前知识库，"
        if context.strip():
            return lead + "我暂时没有接入外部大模型，因此先给你一个基于检索内容的回答：\n\n" + context[:1200], "retrieval-only"
        return "当前知识库里没有找到足够证据回答这个问题。建议先指定一首诗或使用更具体的关键词。", "retrieval-only"
    headers={"Authorization":f"Bearer {settings.llm_api_key}"}
    payload={"model":settings.llm_model,"messages":[{"role":"system","content":prompt}],"temperature":0.2}
    async with httpx.AsyncClient(timeout=45) as client:
        r=await client.post(settings.llm_base_url.rstrip("/")+"/chat/completions",headers=headers,json=payload)
        r.raise_for_status()
        data=r.json()
    return data["choices"][0]["message"]["content"], "llm-rag"
