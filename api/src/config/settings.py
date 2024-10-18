from typing import List, Dict, Optional

from pydantic import BaseSettings, validator

from api.src.utils.cache import Cache
from api.src.utils.database import get_database_url

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str = get_database_url()
    JWT_SECRET_KEY: str
    REDIS_URL: str = "redis://localhost:6379"  # Example Redis URL, adjust as needed
    CELERY_BROKER_URL: str = "redis://localhost:6379"  # Example Celery Broker URL
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379"  # Example Celery Result Backend URL
    LOG_LEVEL: str = "INFO"
    DEV_MODE: bool = True
    CACHE_EXPIRATION_SECONDS: int = 3600  # Example expiration time, adjust as needed

    @validator("OPENAI_API_KEY")
    def validate_openai_api_key(cls, v):
        if not v:
            raise ValueError("OPENAI_API_KEY must be provided.")
        return v

    @validator("JWT_SECRET_KEY")
    def validate_jwt_secret_key(cls, v):
        if not v:
            raise ValueError("JWT_SECRET_KEY must be provided.")
        return v

    @property
    def cache(self) -> Cache:
        return Cache(self.REDIS_URL, self.CACHE_EXPIRATION_SECONDS)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()