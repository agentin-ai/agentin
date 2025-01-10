from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    REDIS_URL: str
    DATABASE_URL: str
    
    class Config:
        env_file = ".env" 