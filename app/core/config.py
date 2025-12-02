from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class DBConfig(BaseModel):
    url: str = getenv("DB_URL")
    echo: bool = False


class SRVConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    reload_on_save: bool = True


class APIConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    srv: SRVConfig = SRVConfig()
    api: APIConfig = APIConfig()


settings = Settings()
