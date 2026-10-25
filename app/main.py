from fastapi import Depends, FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from app.dbsqllite import RatesDB
from app.schemas import *

app = FastAPI()

db = RatesDB()


@app.get("/rate", response_model = AssetResponse)
def get_asset_time_series(body: AssetRequest = Depends()):
    '''
    Launch the get request given an initial date, end date, and rate name. 
    '''
    asset = db.TS_get(body)
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given info not availables"
        )
    else:
        return asset

@app.post("/rate")
def post_rate(data: AssetCreate) -> dict[str, int]:
    '''
    Post method allows to create a new line in our database, uploading new info. 
    '''
    new_id = db.insert(data)
    
    return {"new_id": new_id}

# @app.put("/rate", response_model= BaseRate)
# def update_rate(id:int, body: BaseRate):
#     '''
#     Put method allows to update a whole row from a database. 
#     However, it requires all the row to be specified, not just some of the fields.  
#     '''
#     rates[id] = {
#         "date": body.date, 
#         "rate_name": body.rate_name,
#         "value": body.value
#     }
#     return rates[id]

@app.patch("/rate")
def patch_asset(body: AssetUpdate):
    '''
    Patch rate is similar to the put method, but allowing for just updating the fields we want. 
    The body can be set directly in the request body section in the scalar interface 
    '''
    result = db.update(body) 
    return result

# @app.delete("/rate")
# def delete_rate(id: int) -> dict[str, str]:
#     '''
#     Delete a row from our database by its id
#     '''
#     rates.pop(id)
#     return {"detail": f"Rate with the id #{id} has been deleted."}

@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    '''
    Scalar interface for the API. 
    '''
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Financial Data CalAPI"
    )