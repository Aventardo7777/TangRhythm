# Architecture

```text
Next.js Web
   │
   ├── Poetry UI
   ├── Visualization
   ├── Learning
   └── AI Teacher
          │
          ▼
     API / RAG Layer
          │
     ┌────┼─────────┐
     ▼    ▼         ▼
  PostgreSQL Vector  Graph
     │    Search     │
     └────┼──────────┘
          ▼
     Verified Corpus
```

第一阶段可使用结构化 TypeScript 数据启动；生产阶段迁移 PostgreSQL，并增加 embedding/vector search 与知识图谱服务。
