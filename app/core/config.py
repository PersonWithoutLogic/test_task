from typing import List, Optional
from pydantic import BaseSettings, EmailStr, AnyHttpUrl

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Social Network"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    DATABASE_URL: str = "sqlite:///./test.db"
    USERS_OPEN_REGISTRATION: bool = False
    CLEARBIT_API_KEY: Optional[str] = None
    EMAILHUNTER_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()