import asyncio
from abc import ABC, abstractmethod

import pandas as pd
import requests
from sqlalchemy import text
from .tables import equityT, FXT, cryptoT

from .config import settings
from .models import (  # adjust to wherever your models live
    CryptoRecord,
    EquityRecord,
    FXRecord,
)
from .session import SessionLocal, engine

BASE_URL = "https://api.tiingo.com/tiingo"


class TiingoUploader(ABC):
    '''
    Shared logic for every Tiingo asset class: request, validate, upsert into PostgreSQL.

    Subclasses only define what is specific to the asset class:
      - get():     which endpoint to call
      - prepare(): how to reshape the response into the record's fields
      - table, record_model, columns: where and how it is stored
    '''

    table: str                       # default table name
    record_model: type               # pydantic model used for validation
    columns: dict[str, str]          # record field -> DB column
    text_cols: set[str] = {"tk", "name"}
    default_start: str = "2010-01-01"

    def __init__(self, table: str | None = None):
        if table:
            self.table = table
        self.headers = {"Authorization": f"Token {settings.TIINGO_API_KEY}"}

    def _request(self, path: str, params: dict | None = None):
        response = requests.get(
            f"{BASE_URL}/{path}", params=params, headers=self.headers, timeout=30
        )
        response.raise_for_status()
        return response.json()

    # --- asset-specific ----------------------------------------------
    @abstractmethod
    def get(self, ticker: str, start: str) -> pd.DataFrame:
        '''Download raw data for one ticker.'''

    @abstractmethod
    def prepare(self, df: pd.DataFrame, ticker: str) -> pd.DataFrame:
        '''Return a DataFrame whose columns are exactly the record_model fields.'''

    # --- validate ----------------------------------------------------
    def to_records(self, df: pd.DataFrame, ticker: str) -> list[dict]:
        clean = self.prepare(df, ticker)
        clean = clean.astype(object).where(clean.notna(), None)    # NaN -> None (NULL)
        return [self.record_model(**row).model_dump() for row in clean.to_dict("records")]

    # --- save --------------------------------------------------------
    def _sql_type(self, col: str) -> str:
        if col in self.text_cols:
            return "TEXT"
        return "DATE" if col == "date" else "DOUBLE PRECISION"

    async def save(self, records: list[dict]) -> None:
        cols = list(self.columns.values())
        column_defs = ",\n                ".join(
            f"{c} {self._sql_type(c)}" + (" NOT NULL" if c in ("tk", "date") else "")
            for c in cols
        )
        create = text(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                {column_defs},
                PRIMARY KEY (tk, date)
            )
        """)
        updates = ", ".join(f"{c} = EXCLUDED.{c}" for c in cols if c not in ("tk", "date"))
        upsert = text(f"""
            INSERT INTO {self.table} ({", ".join(cols)})
            VALUES ({", ".join(f":{c}" for c in cols)})
            ON CONFLICT (tk, date) DO UPDATE SET {updates}
        """)
        rows = [{col: r[field] for field, col in self.columns.items()} for r in records]
        async with SessionLocal() as session:
            async with session.begin():   # commit on success, rollback on error
                await session.execute(create)
                await session.execute(upsert, rows)   # insert or update if already exists

    # --- run ---------------------------------------------------------
    async def upload(self, ticker: str, start: str | None = None) -> int:
        df = self.get(ticker, start or self.default_start)
        if df.empty:
            return 0
        records = self.to_records(df, ticker)
        await self.save(records)
        return len(records)

    async def upload_many(self, tickers: list[str], start: str | None = None) -> None:
        for tk in tickers:
            try:
                n = await self.upload(tk, start)
                print(f"[{type(self).__name__}] {tk}: {n} rows saved")
            except Exception as e:        # skip a failing ticker, keep going
                print(f"[{type(self).__name__}] {tk} failed: {e!r}")


# ======================================================================
# Equities / ETFs (end of day)
# ======================================================================
class EquityUploader(TiingoUploader):
    table = equityT
    record_model = EquityRecord
    columns = {
        "tk": "tk", "name": "name", "date": "date",
        "exchange": "exchange", "currency": "currency",
        "open": "open", "high": "high", "low": "low", "close": "close",
        "volume": "volume",
        "adjOpen": "adj_open", "adjHigh": "adj_high", "adjClose": "adj_close",
        "adjVolume": "adj_volume",
        "divCash": "div_cash", "splitFactor": "split_factor",
    }
    text_cols = {"tk", "name", "exchange", "currency"}

    PRICE_FIELDS = [
        "open", "high", "low", "close", "volume",
        "adjOpen", "adjHigh", "adjClose", "adjVolume",
        "divCash", "splitFactor",
    ]

    def __init__(self, table: str | None = None, currency: str = "USD"):
        super().__init__(table)
        self.currency = currency   # Tiingo's daily endpoint does not return the currency

    def get(self, ticker: str, start: str) -> pd.DataFrame:
        # without startDate Tiingo returns only the last day
        data = self._request(f"daily/{ticker}/prices", {"startDate": start, "format": "json"})
        return pd.DataFrame(data)

    def prepare(self, df: pd.DataFrame, ticker: str) -> pd.DataFrame:
        '''
        Add the meta data to the table for the specific ticker
        '''
        meta = self._request(f"daily/{ticker}")   # name and exchange live in the meta endpoint
        out = df[self.PRICE_FIELDS].copy()
        out["tk"] = ticker.upper()
        out["name"] = meta["name"]
        out["exchange"] = meta["exchangeCode"]
        out["currency"] = self.currency
        out["date"] = pd.to_datetime(df["date"]).dt.date
        return out


# ======================================================================
# FX (top-of-book quote: bid / ask / mid)
# ======================================================================
class FXUploader(TiingoUploader):
    '''
    FXRecord is quote based (bid/ask), so this uses Tiingo's top-of-book endpoint.
    It is a snapshot: each daily run stores the latest quote of that day (one row per
    pair and date). History is built up by running the job every day.
    '''
    table = FXT
    record_model = FXRecord
    columns = {
        "tk": "tk", "name": "name", "date": "date",
        "bid": "bid", "bid_size": "bid_size",
        "ask": "ask", "ask_size": "ask_size",
        "mid": "mid",
    }

    def get(self, ticker: str, start: str | None = None) -> pd.DataFrame:
        return pd.DataFrame(self._request("fx/top", {"tickers": ticker}))

    def prepare(self, df: pd.DataFrame, ticker: str) -> pd.DataFrame:
        out = df.rename(columns={
            "bidPrice": "bid", "bidSize": "bid_size",
            "askPrice": "ask", "askSize": "ask_size",
            "midPrice": "mid",
        })[["bid", "bid_size", "ask", "ask_size", "mid"]].copy()
        out["tk"] = ticker.upper()
        out["name"] = ticker.upper()
        out["date"] = pd.to_datetime(df["quoteTimestamp"]).dt.date
        return out


# ======================================================================
# Crypto (daily bars)
# ======================================================================
class CryptoUploader(TiingoUploader):
    table = cryptoT
    record_model = CryptoRecord
    columns = {
        "tk": "tk", "name": "name", "date": "date",
        "base_ccy": "base_ccy", "quote_ccy": "quote_ccy",
        "open": "open", "high": "high", "low": "low", "close": "close",
        "trades_done": "trades_done", "volume": "volume",
        "volume_notional": "volume_notional",
    }
    text_cols = {"tk", "name", "base_ccy", "quote_ccy"}
    default_start = "2015-01-01"

    def get(self, ticker: str, start: str) -> pd.DataFrame:
        data = self._request(
            "crypto/prices",
            {"tickers": ticker, "startDate": start, "resampleFreq": "1day"},
        )
        if not data or not data[0].get("priceData"):
            return pd.DataFrame()
        item = data[0]
        df = pd.DataFrame(item["priceData"])
        df["base_ccy"] = item["baseCurrency"].upper()
        df["quote_ccy"] = item["quoteCurrency"].upper()
        return df

    def prepare(self, df: pd.DataFrame, ticker: str) -> pd.DataFrame:
        out = df.rename(columns={
            "tradesDone": "trades_done",
            "volumeNotional": "volume_notional",
        })[["open", "high", "low", "close", "trades_done", "volume",
            "volume_notional", "base_ccy", "quote_ccy"]].copy()
        out["tk"] = ticker.upper()
        out["name"] = ticker.upper()
        out["date"] = pd.to_datetime(df["date"]).dt.date
        return out


# ======================================================================
# Pick the class by asset class
# ======================================================================
UPLOADERS: dict[str, type[TiingoUploader]] = {
    "equity": EquityUploader,
    "fx": FXUploader,
    "crypto": CryptoUploader,
}


def get_uploader(asset_class: str, **kwargs) -> TiingoUploader:
    try:
        return UPLOADERS[asset_class.lower()](**kwargs)
    except KeyError:
        raise ValueError(f"Unknown asset class {asset_class!r}. Use one of {list(UPLOADERS)}")


async def main():
    jobs = {
        "equity": ["SPY", "AAPL", "MSFT"],
        "fx": ["eurusd", "usdjpy"],
        "crypto": ["btcusd", "ethusd"],
    }
    for asset_class, tickers in jobs.items():
        await get_uploader(asset_class).upload_many(tickers)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())