from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import make_url

def _to_asyncpg(raw: str) -> str:
    """
    Turn a Neon URL into a SQLAlchemy+asyncpg URL.
    
    Why it’s needed:
        Neon gives you strings like postgresql://...?sslmode=require&channel_binding=require. That format is built for libpq-style tools (psql, pg_dump, psycopg2). Your engine is async and uses asyncpg, which breaks on two things:
        The scheme. With a plain postgresql://, SQLAlchemy picks the sync driver (psycopg2), and create_async_engine fails. It needs postgresql+asyncpg://.
        The query parameters. asyncpg doesn’t know sslmode or channel_binding. SQLAlchemy passes them straight through as connect arguments, and you’d get an error like connect() got an unexpected keyword argument 'sslmode'. asyncpg’s equivalent is ssl=require.

        _to_asyncpg does that translation: it swaps the driver name, drops the two unsupported parameters and adds ssl=require.
    
    """
    url = make_url(raw).set(drivername="postgresql+asyncpg")
    # asyncpg doesn't understand sslmode / channel_binding
    query = {k: v for k, v in url.query.items() if k not in ("sslmode", "channel_binding")}
    query["ssl"] = "require"
    return url.set(query=query).render_as_string(hide_password=False)


class DataBaseSettings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PRICES_DB: str
    FRED_API_KEY: str
    TIINGO_API_KEY: str

    # Neon configuration:
    DATABASE_URL: str | None = None
    DATABASE_URL_POOLED: str | None = None 

    model_config = SettingsConfigDict(
        env_file= "./.env",
        env_ignore_empty=True,
        extra="ignore",
        
    )

    @property
    def _local_url(self):
        '''
        The property decorator allows to access this method as a class variable. 
        '''
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_PRICES_DB}"

    @property
    def POSTGRES_URL(self) -> str:
        """Used by the API: pooled > direct > local."""
        raw = self.DATABASE_URL_POOLED or self.DATABASE_URL
        return _to_asyncpg(raw) if raw else self._local_url

    @property
    def POSTGRES_URL_DIRECT(self) -> str:
        """Used by ingestion/migrations: direct > local."""
        return _to_asyncpg(self.DATABASE_URL) if self.DATABASE_URL else self._local_url

settings = DataBaseSettings()
 
