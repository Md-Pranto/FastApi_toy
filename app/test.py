from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def base():
    return {"Welcome to fastapi"}

class Mango(str ,Enum):
    harivanga = "harivanga"
    himsagor = "himsagor"
    fajli = "fajli"

@app.get("/mango/{mango_type}")
async def mango_type(mango:Mango):
    if mango == Mango.fajli:
        return {"I love that"}
    elif mango == Mango.harivanga:
        return {"Oukat se bahar he"}

    if mango.value =="himsagor":
        return {"underrated aam vai"}

class Mango_des(BaseModel):
    name : str
    description: str | None = None
    price : float
    vat : float | None = None

@app.post("/mango/details/{mango_id}")
async def mango_details(mango_id: int ,mango:Mango_des):

    if mango.vat is not None:
        price_with_vat = mango.price + mango.vat
        mango_dump = {"price with vat ": price_with_vat,
                        "mango_id": mango_id,
                        **mango.model_dump()
                      }
    return mango_dump



@app.get("/item_details/{item_id}")
async def item_details(item_id:int, q :int =0 , skip : int =10):
    return {"item_id = " + str(item_id) + str(q) + " " + str(skip)}