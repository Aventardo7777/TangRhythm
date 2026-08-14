from pydantic import BaseModel, Field

class AuthorOut(BaseModel):
    id: int
    name: str
    period: str | None = None
    birth_year: int | None = None
    death_year: int | None = None
    bio: str | None = None
    model_config = {"from_attributes": True}

class PoemSummary(BaseModel):
    id: str
    title: str
    author: str | None
    dynasty: str
    period: str | None
    genre: str | None
    theme: list[str] = Field(default_factory=list)
    emotion: list[str] = Field(default_factory=list)
    content: str

class PoemOut(PoemSummary):
    translation: str | None = None
    annotation: str | None = None
    background: str | None = None
    appreciation: str | None = None
    imagery: list[str] = Field(default_factory=list)
    literary_devices: list[str] = Field(default_factory=list)
    famous_lines: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    difficulty: str
    source_url: str | None = None
    source_name: str | None = None
    author_detail: AuthorOut | None = None

class SearchResult(BaseModel):
    results: list[PoemSummary]
    total: int

class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=3000)
    poem_id: str | None = None
    learner_stage: str = "高中"
    mode: str = "explain"

class Citation(BaseModel):
    title: str
    source: str | None = None
    poem_id: str | None = None
    chunk_type: str | None = None

class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    mode: str
    retrieval_mode: str
