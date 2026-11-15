from datetime import date

from pydantic import BaseModel, Field
from enum import Enum

from ..models.val_models import OptionalPositiveDecimal
from ..static_data.tables import *


class TSUniverse(str, Enum):
    '''
    Asset class mapping to tables
    '''
    Equity = equityT
    FX = FXT
    Crypto = cryptoT
    Macro = macroT

class CandleUniverse(str, Enum):
    '''
    Asset class mapping to tables
    '''
    Equity = equityT
    Crypto = cryptoT

class PriceData(BaseModel):
    '''
    Basic price data model for the most simple get
    '''
    tk: str
    date: date #= Field(..., description="The date of the price bar in YYYY-MM-DD format.")
    close: OptionalPositiveDecimal 

class PriceBar(PriceData):
    '''
    Candlestick data validation model
    '''
    open: OptionalPositiveDecimal 
    high: OptionalPositiveDecimal 
    low: OptionalPositiveDecimal 
    volume: OptionalPositiveDecimal 

