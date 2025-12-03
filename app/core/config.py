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


class APIV1(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"


class APIConfig(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()

    @property
    def bearer_token_to_url(self):
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str = getenv("RESET_PASSWORD_TOKEN_SECRET")
    verification_token_secret: str = getenv("VERIFICATION_TOKEN_SECRET")


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    srv: SRVConfig = SRVConfig()
    api: APIConfig = APIConfig()
    access_token: AccessToken = AccessToken()


settings = Settings()
