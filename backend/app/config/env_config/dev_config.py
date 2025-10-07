from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class DevConfig(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str
    DEBUG: bool
    PORT: int
    HOST: str
    SK: str
    ALGO: str
    
    # redis congiguration
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DECODE_RESPONSE: bool = True
    REDIS_USERNAME: str
    REDIS_PASSWORD: str 
    
    model_config = SettingsConfigDict(env_file="../../../.env")

dev_config = DevConfig()