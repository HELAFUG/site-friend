from fastapi import APIRouter
from core.config import settings
from .auth import auth_router

v1_router = APIRouter(prefix=settings.api.v1.prefix)


v1_router.include_router(router=auth_router)
