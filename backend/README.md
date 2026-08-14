# TangRhythm FastAPI Backend

## Endpoints

- `GET /health`
- `GET /api/poems`
- `GET /api/poems/search?q=李白`
- `GET /api/poems/{poem_id}`
- `POST /api/ai/ask`

## Start with Docker

```bash
docker compose up --build
```

Then:

```bash
curl http://localhost:8000/health
```

## Import the anthology

```bash
cd backend
python scripts/import_tang_poetry.py
```

The importer records source URL and source SHA256. It does not invent modern translations or literary analysis. Those fields are populated later by a separate verified enrichment pipeline.

## AI enrichment

`python scripts/enrich_poems.py` 会生成待人工审核的 JSONL，不会自动覆盖正式数据库教育字段。
