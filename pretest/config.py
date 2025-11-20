from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DatabaseSettings(BaseSettings):
    DB_ENGINE: str = 'django.db.backends.postgresql'
    DB_NAME: str = 'postgres'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'postgres'  # noqa: S105
    DB_PORT: str = '5432'
    DB_HOST: str = 'localhost'


class AuthenticationSettings(BaseSettings):
    ACCEPTED_TOKEN: tuple[str] = ('omni_pretest_token',)


class SystemSettings(BaseSettings):
    SECRET_KEY: str = 'default-key'  # noqa: S105
    DEBUG: bool = True
    ALLOWED_HOSTS: tuple[str] = ('*',)


class Settings(DatabaseSettings, SystemSettings, AuthenticationSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        extra='ignore',
    )


settings = Settings()
