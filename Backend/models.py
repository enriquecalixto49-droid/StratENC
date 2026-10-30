from datetime import date, datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field, model_validator


class BaseRecord(BaseModel):
    '''
    Basic minimal information. 
    Ticker and date. 
    '''
    TK: str
    Date: datetime

class MacroRecord(BaseRecord):
    '''
    Value of the macroeconomic indicator
    '''
    Value: float | None

class FX(BaseRecord):
    '''
    Value of the FX rate
    '''
    fxrate: float | None = Field(gt=0)

class Equity(BaseRecord):
    '''
    Information for equities
    '''
    Currency: str
    Open: float | None = Field(gt=0)
    Close: float| None = Field(gt=0)
    High: float| None = Field(gt=0)
    Low: float| None = Field(gt=0)
    Volume: float| None = Field(gt=0)

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
    currency: str = Field(min_length=3, max_length=3)
    coupon: Decimal = Field(ge=0)          # annual rate, 0 for zero-coupon
    rating: str
    coupon_frequency: int = Field(ge=0)    # payments per year
    issue_date: date
    maturity_date: date
    day_count: DayCount
    face_value: Decimal = Field(gt=0)
    clean_price: float | None = Field(default=None, gt=0) 
    yield_to_maturity: float | None = None
    accrued_interest: float | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def maturity_after_issue(self):
        if self.maturity_date <= self.issue_date:
            raise ValueError("maturity_date must be after issue_date")
        return self




