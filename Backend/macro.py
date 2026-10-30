import asyncio

import pandas as pd
import requests
from sqlalchemy import text

from .config import settings
from .models import MacroRecord  # adjust to wherever your models live
from .session import SessionLocal, engine
from .tables import macroT

class FredUploader:
    '''
    Downloads FRED macroeconomic series and upserts them into PostgreSQL.
    '''

    URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self, table: str = macroT):
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
            "tk": series_id,
            "name": series_id,            # tp be changed when uploading from dictionary
            "date": df["date"],
            "value": pd.to_numeric(df["value"], errors="coerce"),  # FRED's "." -> NaN
        })
        clean = clean.astype(object).where(clean.notna(), None)    # NaN -> None (NULL)
        return [MacroRecord(**row).model_dump() for row in clean.to_dict("records")]

    # --- save --------------------------------------------------------
    async def save(self, records: list[dict]) -> None:
        create = text(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                tk    TEXT NOT NULL,
                name  TEXT NOT NULL,
                date  TIMESTAMP NOT NULL,
                value DOUBLE PRECISION,
                PRIMARY KEY (tk, date)
            )
        """)
        upsert = text(f"""
            INSERT INTO {self.table} (tk, name, date, value)
            VALUES (:tk, :name, :date, :value)
            ON CONFLICT (tk, date) DO UPDATE SET name = EXCLUDED.name, value = EXCLUDED.value
        """)
        async with SessionLocal() as session:
            async with session.begin():   # commit on success, rollback on error
                await session.execute(create)
                await session.execute(upsert, records)

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
    uploader = FredUploader()
    await uploader.upload_many(["DGS10", "DGS2", "FEDFUNDS"])
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())