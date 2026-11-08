from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from ..core.session import SessionLocal


async def get_session() -> AsyncIterator[AsyncSession]:
    '''
    Each request gets its own session, and it is closed automatically when the request ends, even if an error occurs.
    Endpoints declare it with session: AsyncSession = Depends(get_session).
    '''
    async with SessionLocal() as session:
        yield session