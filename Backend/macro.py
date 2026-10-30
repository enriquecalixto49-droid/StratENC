import asyncio

import pandas as pd
import requests
from sqlalchemy import text

from .config import settings
from .models import MacroRecord  # adjust to wherever your models live
from .session import SessionLocal, engine


class FredUploader:
    '''
    Downloads FRED macroeconomic series and upserts them into PostgreSQL.
    '''

    URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self, table: str = "macro_data"):
        self.table = table

    # --- get ---------------------------------------------------------
    def get(self, series_id: str) -> pd.DataFrame:
        params = {
            "series_id": series_id,
            "api_key": settings.FRED_API_KEY,
            "file_type": "json",
        }
        response = requests.get(self.URL, params=params, timeout=30)
        response.raise_for_status()
        return pd.DataFrame(response.json()["observations"])

    # --- validate ----------------------------------------------------
    def to_records(self, df: pd.DataFrame, series_id: str) -> list[dict]:
        clean = pd.DataFrame({
            "TK": series_id,
            "Date": df["date"],
            "Value": pd.to_numeric(df["value"], errors="coerce"),  # FRED's "." -> NaN
        })
        clean = clean.astype(object).where(clean.notna(), None)    # NaN -> None (NULL)
        return [MacroRecord(**row).model_dump() for row in clean.to_dict("records")]

    # --- save --------------------------------------------------------
    async def save(self, records: list[dict]) -> None:
        create = text(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                tk    TEXT      NOT NULL,
                date  TIMESTAMP NOT NULL,
                value DOUBLE PRECISION,
                PRIMARY KEY (tk, date)
            )
        """)
        upsert = text(f"""
            INSERT INTO {self.table} (tk, date, value)
            VALUES (:TK, :Date, :Value)
            ON CONFLICT (tk, date) DO UPDATE SET value = EXCLUDED.value
        """)
        async with SessionLocal() as session:
            async with session.begin():   # commit on success, rollback on error
                await session.execute(create)
                await session.execute(upsert, records) # insert or update if already exists

    # --- run ---------------------------------------------------------
    async def upload(self, series_id: str) -> int:
        records = self.to_records(self.get(series_id), series_id)
        await self.save(records)
        return len(records)

    async def upload_many(self, series_ids: list[str]) -> None:
        for sid in series_ids:
            try:
                n = await self.upload(sid)
                print(f"{sid}: {n} rows saved")
            except Exception as e:        # skip a failing series, keep going
                print(f"{sid} failed: {e!r}")


async def main():
    uploader = FredUploader(settings.POSTGRES_FRED_DB)
    await uploader.upload_many(["DGS10", "DGS2", "FEDFUNDS"])
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())