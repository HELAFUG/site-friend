import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.helpers import db_helper
from core.config import settings
from api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=settings.srv.reload_on_save,
    )
