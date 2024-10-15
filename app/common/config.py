from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env file

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
