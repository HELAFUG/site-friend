from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Profile


async def get_profile(session: AsyncSession, user_id: int):
    stmt = select(Profile).where(Profile.user_id == user_id)
    res = await session.execute(stmt)
    return res.scalars().first()


async def create_profile(
    session: AsyncSession,
    user_id: int,
    name: str,
    available: bool,
    wish_to_walk: int,
    preority: int,
) -> Profile:
    profile_exists = await get_profile(session, user_id)
    if profile_exists:
        return profile_exists

    profile = Profile(
        user_id=user_id,
        name=name,
        available=available,
        wish_to_walk=wish_to_walk,
        preority=preority,
    )
    session.add(profile)
    await session.commit()

    return profile
