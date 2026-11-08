from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from ..deps import get_session
from ..schemas import Universe, PriceData

router = APIRouter(tags=["Prices"], prefix="/prices")

@router.get("/{asset_class}/{tk}", response_model=list[PriceData])
async def prices(
    asset_class: Universe, 
    tk  : str, 
    start: date | None = None , 
    end: date | None = None, 
    limit: int = Query(10000, le=10000, ge=1), # specifies that is a query parameter, and set a default value and a limit (le, ge, lt, ...)
    session: AsyncSession = Depends(get_session),
    ):
    """
    Get price data for a given asset class and ticker between start and end dates.
    """
    if start > end:
        raise HTTPException(422, "start must be on or before end")
    
    table_name = asset_class.value
    query = text(f"""
        SELECT date, value
        FROM {table_name}
        WHERE tk = :ticker AND date BETWEEN :start AND :end
        ORDER BY date
        LIMIT :limit
    """)

    # Generate a result object (a cursor over the rows)
    result = await session.execute(query, {"ticker": tk, "start": start, "end": end, "limit": limit})

    # Check if there are any rows returned. If not, return an empty list.
    rows = result.fetchall()
    if not rows:
        return []
        
    return result.mappings().all() # fetch them all into a Python list of dictionaries, where each dictionary represents a row with column names as keys.

