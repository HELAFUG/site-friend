from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer


from core.models import Base
from core.models.mixins import IdIntPkMixin

if TYPE_CHECKING:
    from core.models import Profile


class Shedule(Base, IdIntPkMixin):
    profile_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("profiles.id", ondelete="CASCADE")
    )
    profile: Mapped["Profile"] = relationship(back_populates="shedule")

    monday: Mapped[bool]
    tuesday: Mapped[bool]
    wednesday: Mapped[bool]
    thursday: Mapped[bool]
    friday: Mapped[bool]
    saturday: Mapped[bool]
    sunday: Mapped[bool]
