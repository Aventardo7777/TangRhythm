from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import UserDefinedType
from app.core.config import settings

engine = create_async_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class VectorType(UserDefinedType):
    cache_ok = True
    def __init__(self, dimensions: int = 1536):
        self.dimensions = dimensions
    def get_col_spec(self, **kw):
        return f"VECTOR({self.dimensions})"
    def bind_processor(self, dialect):
        def process(value):
            if value is None: return None
            return "[" + ",".join(str(float(x)) for x in value) + "]"
        return process
    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None: return None
            if isinstance(value, str):
                return [float(x) for x in value.strip("[]").split(",") if x.strip()]
            return value
        return process

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
