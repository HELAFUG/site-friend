import logging
from typing import TYPE_CHECKING
from typing import Optional
from fastapi_users import (
    BaseUserManager,
    IntegerIDMixin,
)

from core.config import settings
from core.models import User
from core.config import settings


if TYPE_CHECKING:
    from fastapi import Request
    from fastapi import Response
    from fastapi import BackgroundTasks

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    def __init__(
        self,
        user_db,
        password_hasher=None,
        background_tasks: Optional["BackgroundTasks"] = None,
    ):
        super().__init__(user_db, password_hasher)
        self.background_tasks = background_tasks

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning("User registered %r", user.id)

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning("Verification requested for user %r, token %r", user.id, token)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning("Forgot password requested for user %r", user.id)

    async def on_after_reset_password(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning("Reset password requested for user %r", user.id)

    async def on_after_verify(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning("Verification requested for user %r", user.id)

    async def on_after_login(
        self,
        user: User,
        request: Optional["Request"] = None,
        response: Optional["Response"] = None,
    ):
        log.warning("Login requested for user %r", user.id)
