from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class DBConfig(BaseModel):
    url: str = getenv("DB_URL")
    echo: bool = False
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


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
