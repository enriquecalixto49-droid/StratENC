from sqlmodel import SQLModel, Field

class AssetMinimal(SQLModel, table = True):
    '''
    table = True is essential. if we don't pass it, it is like a basemodel from pydantic. 
    '''
    __tablename__ = 'ENC_AssetDB'

    id: int = Field(default = None, primary_key= True)
    date: str = Field(max_length=8)
    name: str 
    value: float
