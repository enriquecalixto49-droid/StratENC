from pydantic import BaseModel, Field
from typing import Any

class BaseRate(BaseModel):
    '''
    Pydantic BaseModel will perform all data validation for us by defining the class attributes beforehans 
    With field, we can even perform some checks (le -> lower or equal )

    BaseRate will be the minimal data to be read/provided. That is:
    - date
    - rate
    - value 
    '''
    date: str = Field(max_length=8) # max len for dates is 8 yyyymmdd 
    name: str
    value: float = Field(le=1) # max rate is 100%

class AssetRequest(BaseModel):
    '''
    Usual request model for an asset. 

    - Initial date
    - End date
    - Name of the asset 
    '''
    db_name: str
    init_date: str 
    end_date: str 
    name: str  # key is the date, value will be the rate 

class AssetCreate(BaseModel):
    '''
    Inserting rows in the database
    '''
    db_name: str
    date: str
    name: str
    value: float

class AssetUpdate(BaseModel):
    '''
    Updata a row in a the database
    '''
    db_name: str
    field_to_set: str
    value: Any
    condition: str

class AssetResponse(BaseModel):
    '''
    Response model for the requests. 

    Usually, people will want to get data from one date to another. Thus, we will return
    - Request type verification.
    - Initial and end dates
    - The name of the rate
    - The values of the time series. 
    '''
    request: str 
    initial_date: str 
    end_date: str
    name: str 
    values: dict[str, float] # key is the date, value will be the rate 



    