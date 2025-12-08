import logging
from typing import Annotated, TYPE_CHECKING
from taskiq import TaskiqDepends
from sqlalchemy.ext.asyncio import AsyncSession
from service.mailing.mail import send_welcome_admin
from core.helpers import db_helper
from core.models import User
from core import broker
from repository.user import get_user_by_id

log = logging.getLogger(__name__)


@broker.task
async def send_welcome_admin(
    user_id: int,
    session: Annotated[AsyncSession, TaskiqDepends(db_helper.session_getter)],
):
    user = await get_user_by_id(
        session=session,
        user_id=user_id,
    )
    log.info("Sending admin email for user %r", user.id)
    await send_welcome_admin(user=user)
