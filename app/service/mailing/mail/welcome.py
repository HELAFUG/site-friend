from core.models import User
from service.mailing.mail.send_mail import send_email


async def send_welcome_email(user: User) -> None:
    await send_email(
        recipient=user.email,
        sub="Welcome to Friend Walk Service",
        body="Thanks for signing up",
    )


async def send_welcome_admin(user: User) -> None:
    await send_email(
        recipient=user.email,
        sub="Welcome to Friend Walk Service,You are new admin",
        body="Thanks for using Friend Walk Service",
    )
