from sqlalchemy import text

from Backend.models import StaticData
from Backend.session import SessionLocal
from .fred_macro import FRED_MACRO_SERIES
from .tiingo_crypto import TIINGO_CRYPTO_SERIES
from .tiingo_equity import TIINGO_EQUITY_SERIES
from .tiingo_fx import TIINGO_FX_SERIES
from Backend.tables import FXS, cryptoS, equityS, macroS

STATIC_TABLES: dict[str, dict] = {
    macroS: FRED_MACRO_SERIES,
    equityS: TIINGO_EQUITY_SERIES,
    FXS: TIINGO_FX_SERIES,
    cryptoS: TIINGO_CRYPTO_SERIES
}

class StaticUploader:
    '''
    Uploads static data for financial instruments into PostgreSQL.
    '''

    def __init__(self, table: str):
        self.table = table

    def to_records(self, data: dict) -> list[dict]:
        '''
        Transforms a dictionary of static data into a list of records suitable for database insertion.
        Each record is a dictionary with keys 'tk', 'name', and 'category'.
        '''
        pairs = [(tk, name, cat) for cat, items in data.items() for tk, name in items.items()]

        seen: set[str] = set()
        for tk, _, cat in pairs:
            # Raise an error if a ticker is duplicated across categories or within the same category
            if tk in seen:
                raise ValueError(f"Duplicate ticker {tk!r} (category {cat!r})")
            seen.add(tk)

        return [StaticData(tk=tk, name=name, category=cat).model_dump() for tk, name, cat in pairs]

    
    async def save(self, records: list[dict]) -> None:
        create = text(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                tk    TEXT NOT NULL,
                name  TEXT NOT NULL,
                category TEXT,
                PRIMARY KEY (tk)
            )
        """)
        upsert = text(f"""
            INSERT INTO {self.table} (tk, name, category)
            VALUES (:tk, :name, :category)
            ON CONFLICT (tk) DO UPDATE SET name = EXCLUDED.name, category = EXCLUDED.category
        """)
        async with SessionLocal() as session:
            await session.execute(create)
            await session.execute(upsert, records)
            await session.commit()
