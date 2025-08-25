from typing import Union
from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_cute: Union[bool, None] = None

class PostCard(BaseModel):
    address: str
    date: date
    card_body_text: str
    is_signed: bool

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, 
            "q": q, 
            "some_id": f'this is the id #{item_id}'}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return { "message": "200 Successful update", 
            "item_name" : item.name, 
            "how much?": item.price,
            "item_id": item_id }

@app.post("/postcards")
async def create_postcard(postcard: PostCard):
    return { "message": "200 Card posted!",
            "payload" : f'On {str(postcard.date)} sent at {postcard.address} text: {postcard.card_body_text} signed: {'xoxo' if postcard.is_signed else 'oops forgot to sign :['}'
            }

#TODO app.delete concept and example