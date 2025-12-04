from fastapi import APIRouter
from core.config import settings
from core.schemas.user import UserCreate, UserRead
from api.dependencies.authentication import authentication_backend
from .fastapi_users import fastapi_users

auth_router = APIRouter(prefix=settings.api.v1.auth)
auth_router.include_router(
    fastapi_users.get_auth_router(backend=authentication_backend)
)
auth_router.include_router(
    fastapi_users.get_register_router(
        user_create_schema=UserCreate, user_schema=UserRead
    )
)
