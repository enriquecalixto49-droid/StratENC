from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from sqlalchemy import text

from ..core.session import engine_api
from .routers.prices import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # One connection per request and shutdown when finished

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
