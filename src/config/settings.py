from pydantic_settings import BaseSettings

__all__ = ['settings']

class Settings(BaseSettings):
    GOOGLE_GEOCODE_API_KEY: str
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    API_SECRET_KEY: str


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
