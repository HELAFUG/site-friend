from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship
from core.models import Base
from core.models.mixins import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .access_token import AccessToken
    from .profile import Profile


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    access_tokens: Mapped[list["AccessToken"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
