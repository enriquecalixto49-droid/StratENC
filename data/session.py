from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from .config import settings

# Create a database engine to connect with the database
engine: AsyncEngine = create_async_engine(
    url= settings.POSTGRES_URL,
    echo = True #Log SQL queries
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,  # keeps objects usable after commit
)