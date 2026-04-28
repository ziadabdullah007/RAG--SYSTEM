from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

BASE_DIR = Path(__file__).resolve().parents[2]  # يرجع لجذر المشروع

class Settings(BaseSettings):
    app_name: str
    app_version: str
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env")  # 👈 أهم سطر
    )


@lru_cache
def get_settings():
    return Settings()
