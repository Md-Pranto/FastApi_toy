from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class FruitName(str,Enum):
    banana = "banana"
    orange = "orange"
    mango  = "mango"


app = FastAPI()


@app.get("/")
async def root():
    return {"hello"}

@app.get("/ask")
async def ask():
    return {"ki ask korbo vai ?"}

@app.get("/item/{item_id}")
async def read_item(item_id : int):
    return {"item_id": str(item_id) + " Adittya"}

@app.get("/user/me")
async def read_user_me():
    return {"user_id ": "the current user"}

# parameter
@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"user_id ": user_id}

# Enum
@app.get("/fruit/{fruit_name}")
async def read_fruit(fruit_name : FruitName):
    if fruit_name is FruitName.banana:
        return {"ami kintu lomba bro ..." : fruit_name}
    elif fruit_name is FruitName.orange:
        return {"I am really orange in color": fruit_name}

    if fruit_name.value == "mango":
        return{"I am sweet brother" : FruitName.mango}

# Extract Path
@app.get("/path/{file_path:path}")
async def read_path(file_path: str):
    return {"file_path" : file_path}

#Query Parameter

fake_items_db = [
    {"item name ": "Halim"},
    {"item name ": "piyaju"},
    {"item name ": "Bar"}
]

# @app.get("/items/{num}")
# async def read_item(num:int,skip: int , limit: int=1):
#     return fake_items_db[skip+num : skip+ limit]

@app.get("/item_check/{item_id}")
async def read_item(
    item_id: str,
    q: str | None = None,
    short: bool = False
    ):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Post Request
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items")
async def get_item(item: Item):
    item_dict = item.model_dump()

    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}