# TangRhythm

> **让古诗词不只是被背下来，而是被真正理解。**

TangRhythm 是一个融合中国古典文学、数据科学、知识图谱、交互式可视化与生成式 AI 的数字人文智能教学平台。第一阶段聚焦《唐诗三百首》，面向学生、家长与教师，提供诗歌阅读、语义搜索、AI 讲诗、知识探索、统计分析与学习分析。

## Product

**Data → Knowledge → Intelligence → Visualization → Education**

- Poetry Explorer：诗歌、作者、主题、意象与名句
- AI Teacher：按小学 / 初中 / 高中 / 深度模式讲诗
- Knowledge Graph：作者、诗歌、意象、主题、情感、地点、历史事件
- Visualization：主题、情绪、意象共现、作者关系与地域
- Learning Analytics：收藏、背诵、测验、复习与 Mastery Score
- Teacher / Parent：备课与家庭辅导场景

## Current MVP

本仓库提供一个可运行的 Next.js + TypeScript 前端 MVP，并预留 FastAPI、RAG、向量检索、PostgreSQL 与 Neo4j 扩展接口。

> 教育内容应以可靠来源校验为准。本 MVP 使用少量示例数据作为结构化数据演示，不声称已经收录完整《唐诗三百首》。

## Tech Stack

Next.js · React · TypeScript · Tailwind CSS · Recharts · Python/FastAPI（planned）· PostgreSQL（planned）· RAG（planned）

## Run

```bash
npm install
npm run dev
```

然后打开 `http://localhost:3000`。

## Roadmap

- [x] Premium Oriental UI foundation
- [x] Poetry explorer
- [x] Poem detail
- [x] Theme / emotion / imagery visualization
- [x] Learning dashboard
- [x] Skill specifications
- [ ] Full verified Tang Poetry dataset
- [ ] FastAPI + PostgreSQL
- [ ] RAG retrieval
- [ ] Production AI Teacher
- [ ] Knowledge graph backend
- [ ] Poetry map
- [ ] Teacher / Parent workspaces
- [ ] Spaced repetition
- [ ] Song Ci / Yuan Qu expansion

## Philosophy

> 一卷唐诗，读见千年风华。


## Phase 2 · Data + API + RAG

Phase 2 adds a PostgreSQL/pgvector-ready data model, FastAPI service, reproducible anthology import, and a citation-returning AI Teacher pipeline.

```text
Question
  ↓
Deterministic Retrieval
  ↓
Poem / Author / Background Context
  ↓
Stage-aware Prompt
  ↓
LLM (optional)
  ↓
Answer + Citations
```

The backend works without an LLM key in **retrieval-only** mode, so the product does not invent an answer merely because an API key is missing.

### Start backend

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

Import the anthology after the database is ready:

```bash
docker compose exec api python scripts/import_tang_poetry.py
```

The source importer preserves the source URL and SHA256. It intentionally leaves educational enrichment fields separate from source text. `scripts/enrich_poems.py` produces a reviewable JSONL draft rather than silently writing model output into the canonical corpus.
