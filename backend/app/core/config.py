from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "TangRhythm API"
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://tangrhythm:tangrhythm@localhost:5432/tangrhythm"
    llm_api_key: str | None = None
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4.1-mini"
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536
    cors_origins: str = "http://localhost:3000"
    source_url: str = "https://raw.githubusercontent.com/rime-aca/corpus/master/%E5%94%90%E8%A9%A9%E4%B8%89%E7%99%BE%E9%A6%96.txt"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
