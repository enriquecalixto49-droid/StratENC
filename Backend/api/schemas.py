from pydantic import BaseModel, Field
from sqlalchemy import Enum

from ..static_data.tables import *


class Universe(str, Enum):
    Equity= equityT
    FX= FXT
    Crypto= cryptoT
    Macro= macroT

class PriceBar(BaseModel):
    ticker: str = Field(..., description="The ticker symbol of the asset.")
    date: str = Field(..., description="The date of the price bar in YYYY-MM-DD format.")
    open: float = Field(..., description="The opening price of the asset on the given date.")
    high: float = Field(..., description="The highest price of the asset on the given date.")
    low: float = Field(..., description="The lowest price of the asset on the given date.")
    close: float = Field(..., description="The closing price of the asset on the given date.")
    volume: int = Field(..., description="The trading volume of the asset on the given date.")

