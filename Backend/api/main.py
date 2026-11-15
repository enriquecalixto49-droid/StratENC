from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from sqlalchemy import text

from ..core.session import engine_api
from .routers.prices import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    The engine is a parking lot of database connections. It’s created once, when your app starts, and it holds a few open connections to Neon so they can be reused.
    A session is one person borrowing a connection for a single request. get_session handles that: borrow a connection when the request starts, give it back when the request ends.
    
    So there are two separate things to manage:
        1 - Borrowing and returning, for every request. That’s get_session.
        2 - Opening and closing the whole parking lot, once. That’s lifespan.
    '''
    
    # startup: fail fast if the DB is unreachable
    async with engine_api.begin() as conn:
        await conn.execute(text("SELECT 1"))
    yield
    # shutdown: close the connection pool
    await engine_api.dispose()

app = FastAPI(
    # Server start/stop listener
    lifespan=lifespan,
)

app.include_router(router)

### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
