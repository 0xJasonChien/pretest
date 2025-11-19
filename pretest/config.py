from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DatabaseSettings(BaseSettings):
    DB_ENGINE: str = 'django.db.backends.postgresql'
    DB_NAME: str = 'POSTGRES_NAME'
    DB_USER: str = 'POSTGRES_USER'
    DB_PASSWORD: str = 'POSTGRES_PASSWORD'  # noqa: S105
    DB_PORT: str = 'POSTGRES_PORT'
    DB_HOST: str = 'POSTGRES_HOST'

class AuthenticationSettings(BaseSettings):
    ACCEPTED_TOKEN : tuple[list] = ('omni_pretest_token',)

class SystemSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = ['*']


class Settings(DatabaseSettings, SystemSettings, AuthenticationSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


settings = Settings()
