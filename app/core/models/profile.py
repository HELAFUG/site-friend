from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

from core.models import Base
from core.models.mixins import IdIntPkMixin


if TYPE_CHECKING:
    from core.models import User
    from core.models import Shedule


class Profile(Base, IdIntPkMixin):
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE")
    )
    user: Mapped["User"] = relationship(back_populates="profile")

    name: Mapped[str]
    available: Mapped[bool]
    wish_to_walk: Mapped[int]
    preority: Mapped[int]
    week_shedule: Mapped["Shedule"] = relationship(back_populates="profile")
