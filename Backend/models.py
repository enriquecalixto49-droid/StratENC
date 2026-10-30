from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field, model_validator

OptionalPositiveDecimal = Annotated[Decimal | None, Field(default=None, ge=0)]
CurrencyNotation = Annotated[str, Field(max_length = 3, min_length = 3)]

class BaseRecord(BaseModel):
    '''
    Basic minimal information.

    Ticker: identifier in the financial data service provider
    Name: company/indicator name
    Date: date in date format since we will backtest low frequency (no need for datetime)
    '''
    tk: str
    name: str
    date: date

class MacroRecord(BaseRecord):
    '''
    Value of the macroeconomic indicator
    '''
    value: float | None = None

class FXRecord(BaseRecord):
    '''
    Data for FX Rates
    No exchange for FX data. Tiingo connects directly to 
    tier-1 banks and FX dark pools to provide institutional-grade quality Forex quotes.
    '''
    bid: OptionalPositiveDecimal
    bid_size: OptionalPositiveDecimal
    ask: OptionalPositiveDecimal
    ask_size: OptionalPositiveDecimal
    mid: OptionalPositiveDecimal
    
    @model_validator(mode="after")
    def validate_prices(self):
        '''
        Don't check for mid Price for complexity self-contention (trust Tiingo). 
        To be updated in future upgrades
        '''
        if (
            self.bid is not None
            and self.ask is not None
            and self.ask <= self.bid
        ):
            raise ValueError("Invalid bid-ask relationship")

        return self

class CryptoRecord(BaseRecord):
    base_ccy: CurrencyNotation
    quote_ccy: CurrencyNotation
    open: OptionalPositiveDecimal
    high: OptionalPositiveDecimal
    low: OptionalPositiveDecimal
    close: OptionalPositiveDecimal
    trades_done: OptionalPositiveDecimal
    volume : OptionalPositiveDecimal
    volume_notional: OptionalPositiveDecimal

    @model_validator(mode="after")
    def validate_prices(self):
        if (
            self.high is not None
            and self.low is not None
            and self.high <= self.low
        ):
            raise ValueError("Invalid High-Low relationship")

        if (
            self.high is not None
            and self.low is not None
            and self.open is not None
            and not (self.low <= self.open <= self.high)
        ):
            raise ValueError("Open outside range")

        if (
            self.high is not None
            and self.low is not None
            and self.close is not None
            and not (self.low <= self.close <= self.high)
        ):
            raise ValueError("Close outside range")


        return self

class EquityRecord(BaseRecord):
    '''
    Information for equities
    Adjusted figures are key in a backtesting framework to avoid split/reverse split 
    ficticious returns
    '''
    exchange: str
    currency: CurrencyNotation
    open: OptionalPositiveDecimal
    close: OptionalPositiveDecimal
    high: OptionalPositiveDecimal
    low: OptionalPositiveDecimal
    volume: OptionalPositiveDecimal
    adjClose: OptionalPositiveDecimal
    adjHigh: OptionalPositiveDecimal
    adjOpen: OptionalPositiveDecimal
    adjVolume: OptionalPositiveDecimal
    divCash: OptionalPositiveDecimal
    splitFactor: OptionalPositiveDecimal

    @model_validator(mode="after")
    def validate_prices(self):
        if (
            self.high is not None
            and self.low is not None
            and self.high <= self.low
        ):
            raise ValueError("Invalid High-Low relationship")

        if (
            self.high is not None
            and self.low is not None
            and self.open is not None
            and not (self.low <= self.open <= self.high)
        ):
            raise ValueError("Open outside range")

        if (
            self.high is not None
            and self.low is not None
            and self.close is not None
            and not (self.low <= self.close <= self.high)
        ):
            raise ValueError("Close outside range")

        return self

# Fixed Income Validation (more complex)

class DayCount(str, Enum):
    '''
    Types of date count
    '''
    ACT_360 = "ACT/360"
    ACT_365 = "ACT/365"
    THIRTY_360 = "30/360"
    ACT_ACT = "ACT/ACT"

# Static reference data (one row per bond)
class BondReference(BaseRecord):
    issuer: str
    currency: CurrencyNotation
    coupon: OptionalPositiveDecimal          # annual rate, 0 for zero-coupon
    rating: str
    coupon_frequency: OptionalPositiveDecimal   # payments per year
    issue_date: date
    maturity_date: date
    day_count: DayCount
    face_value: Decimal = Field(ge=0)
    clean_price: OptionalPositiveDecimal
    yield_to_maturity: OptionalPositiveDecimal
    accrued_interest: OptionalPositiveDecimal

    @model_validator(mode="after")
    def maturity_after_issue(self):
        if self.maturity_date <= self.issue_date:
            raise ValueError("maturity_date must be after issue_date")
        return self



