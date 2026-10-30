

import requests
import pandas as pd
from .models import EquityRecord, FXRecord, CryptoRecord

class TiingoUploader:

    URL = "https://api.tiingo.com/tiingo/daily"

    def __init__(self, table: str, universe: str):
        self.table = table
        self.universe = universe

    def get(self, ticker: str) -> pd.DataFrame:

        headers = {
            "Authorization": f"Token {Api_Token}"
        }

        response = requests.get(
            f"{self.URL}/{ticker}/prices",
            headers=headers,
            params={
                "startDate": "2010-01-01",
                "resampleFreq": "daily"
            },
            timeout=30
        )

        response.raise_for_status()

        return pd.DataFrame(response.json())

    def to_records(self, df: pd.DataFrame, ticker: str) -> list[dict]:
        if self.universe == 'equity':
            clean = pd.DataFrame({
                "tk": series_id,
                "date": df["date"],
                "value": pd.to_numeric(df["value"], errors="coerce"),  # FRED's "." -> NaN
                "exchange": 
                "currency": 
                "open": 
                "close": 
                "high": 
                "low": 
                "volume": 
                "adjClose": 
                "adjHigh": 
                "adjOpen": 
                "adjVolume": 
                "divCash": 
                "splitFactor": 
            })
            clean = clean.astype(object).where(clean.notna(), None)    # NaN -> None (NULL)
            return [MacroRecord(**row).model_dump() for row in clean.to_dict("records")]