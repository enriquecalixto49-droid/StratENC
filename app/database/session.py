from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session
from app.config import DataBaseSettings

settings = DataBaseSettings() # No error (just pylance bug)

engine = create_async_engine(
    url = settings.POSTGRES_URL,
    echo = True # To get the sql responses in the terminal. 
                    ) 

async def create_db_tables():
    async with engine.begin() as connection:
        from .models import AssetMinimal
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session():
    '''
    Create and asynchronous session to the PostgreSQL data base 
    '''
    async_session = sessionmaker(
        bind = engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]