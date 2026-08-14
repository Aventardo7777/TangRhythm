from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import VectorType
from app.db.session import Base

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), index=True)
    aliases: Mapped[list[str] | None] = mapped_column(nullable=True)
    birth_year: Mapped[int | None] = mapped_column(Integer)
    death_year: Mapped[int | None] = mapped_column(Integer)
    bio: Mapped[str | None] = mapped_column(Text)
    period: Mapped[str | None] = mapped_column(String(30))
    source: Mapped[str | None] = mapped_column(Text)
    poems: Mapped[list["Poem"]] = relationship(back_populates="author")

class Poem(Base):
    __tablename__ = "poems"
    id: Mapped[str] = mapped_column(String(120), primary_key=True)
    anthology_index: Mapped[int | None] = mapped_column(Integer, index=True)
    title: Mapped[str] = mapped_column(String(120), index=True)
    author_id: Mapped[int | None] = mapped_column(ForeignKey("authors.id", ondelete="SET NULL"), index=True)
    dynasty: Mapped[str] = mapped_column(String(20), default="唐")
    period: Mapped[str | None] = mapped_column(String(20))
    genre: Mapped[str | None] = mapped_column(String(40))
    content: Mapped[str] = mapped_column(Text)
    translation: Mapped[str | None] = mapped_column(Text)
    annotation: Mapped[str | None] = mapped_column(Text)
    background: Mapped[str | None] = mapped_column(Text)
    appreciation: Mapped[str | None] = mapped_column(Text)
    theme: Mapped[list[str] | None] = mapped_column(nullable=True)
    emotion: Mapped[list[str] | None] = mapped_column(nullable=True)
    imagery: Mapped[list[str] | None] = mapped_column(nullable=True)
    literary_devices: Mapped[list[str] | None] = mapped_column(nullable=True)
    famous_lines: Mapped[list[str] | None] = mapped_column(nullable=True)
    keywords: Mapped[list[str] | None] = mapped_column(nullable=True)
    difficulty: Mapped[str] = mapped_column(String(20), default="intermediate")
    school_stages: Mapped[list[str] | None] = mapped_column(nullable=True)
    source_url: Mapped[str | None] = mapped_column(Text)
    source_name: Mapped[str | None] = mapped_column(String(200))
    source_hash: Mapped[str | None] = mapped_column(String(128))
    embedding: Mapped[list[float] | None] = mapped_column(VectorType(1536), nullable=True)
    fts: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    author: Mapped[Author | None] = relationship(back_populates="poems")
    __table_args__ = (UniqueConstraint("title", "author_id", name="uq_poem_title_author"),)

class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    poem_id: Mapped[str | None] = mapped_column(ForeignKey("poems.id", ondelete="CASCADE"), index=True)
    chunk_type: Mapped[str] = mapped_column(String(40), index=True)
    title: Mapped[str] = mapped_column(String(160))
    content: Mapped[str] = mapped_column(Text)
    source_url: Mapped[str | None] = mapped_column(Text)
    embedding: Mapped[list[float] | None] = mapped_column(VectorType(1536), nullable=True)

class LearningRecord(Base):
    __tablename__ = "learning_records"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    learner_id: Mapped[str] = mapped_column(String(120), index=True)
    poem_id: Mapped[str] = mapped_column(ForeignKey("poems.id", ondelete="CASCADE"), index=True)
    action: Mapped[str] = mapped_column(String(40), index=True)
    score: Mapped[float | None] = mapped_column(Float)
    metadata_json: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
