# api/routers/tickers.py
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..deps import get_session
from ..schemas import Universe

router = APIRouter(prefix="/tickers", tags=["tickers"])

@router.get("/{asset_class}", response_model=list[str])
async def list_tickers(asset_class: Universe, session: AsyncSession = Depends(get_session)):
    rows = await session.execute(
        text(f"SELECT DISTINCT tk FROM {asset_class.value} ORDER BY tk")
    )
    return [r[0] for r in rows]