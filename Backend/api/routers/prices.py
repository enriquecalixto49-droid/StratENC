from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from ...static_data.tables import macroT, equityT, FXT, cryptoT
from ..deps import get_session
from ..schemas import TSUniverse, CandleUniverse, PriceData, PriceBar

router = APIRouter(tags=["Prices"], prefix="/prices")

close_data_dict = {
    macroT: 'value',
    equityT: 'adj_close',
    FXT: 'mid',
    cryptoT: 'close'
}

@router.get("/{asset_class}/{tk}", response_model=list[PriceData])
async def prices(
    asset_class: TSUniverse, 
    tk  : str, 
    start: date | None = None , 
    end: date | None = None, 
    limit: int = Query(10000, le=10000, ge=1), # specifies that is a query parameter, and set a default value and a limit (le, ge, lt, ...)
    session: AsyncSession = Depends(get_session),
    ):
    """
    Get price/value data for a given asset class and ticker between start and end dates.
    """
    if start and end and start > end:
        raise HTTPException(422, "start must be on or before end")

    table_name = asset_class.value
    query = text(f"""
        SELECT tk, date, {close_data_dict[table_name]} AS close 
        FROM {table_name}
        WHERE tk = :ticker AND date BETWEEN :start AND :end
        ORDER BY date
        LIMIT :limit
    """)

    # Generate a result object (a cursor over the rows)
    result = await session.execute(query, {"ticker": tk, "start": start, "end": end, "limit": limit})

    # Check if there are any rows returned. If not, return an empty list.
    rows = result.mappings().all() # fetch them all into a Python list of dictionaries, where each dictionary represents a row with column names as keys.
    if not rows:
        raise HTTPException(404, f"No data for {tk}")
        
    return rows


@router.get("/{asset_class}/{tk}/candle", response_model=list[PriceBar])
async def candlestick(
    asset_class: CandleUniverse, 
    tk  : str, 
    start: date | None = None , 
    end: date | None = None, 
    limit: int = Query(10000, le=10000, ge=1), # specifies that is a query parameter, and set a default value and a limit (le, ge, lt, ...)
    session: AsyncSession = Depends(get_session),
    ):
    """
    Get candlestick data for eligible universes
    """
    if start and end and start > end:
        raise HTTPException(422, "start must be on or before end")

    table_name = asset_class.value
    adj = '' if table_name == cryptoT else 'adj_'
    query = text(f"""
        SELECT tk, date, close, {adj}open as open, 
        {adj}high as high, {adj}low as low, {adj}volume as volume 
        FROM {table_name}
        WHERE tk = :ticker AND date BETWEEN :start AND :end
        ORDER BY date
        LIMIT :limit
    """)

    # Generate a result object (a cursor over the rows)
    result = await session.execute(query, {"ticker": tk, "start": start, "end": end, "limit": limit})

    # Check if there are any rows returned. If not, return an empty list.
    rows = result.mappings().all() # fetch them all into a Python list of dictionaries, where each dictionary represents a row with column names as keys.
    if not rows:
        raise HTTPException(404, f"No data for {tk}")
        
    return rows


