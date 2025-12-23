import os
from pydantic_settings import BaseSettings
from pydantic import SecretStr

from dotenv import load_dotenv
load_dotenv('.env')
class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    RUN_MODE: str = ""
    WEBHOOK_URL: str = ""
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Settings()