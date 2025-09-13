from typing import Union
from datetime import date

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
import io

from random import randint
from pydantic import BaseModel

from db import JONS_DB, find_index_by_id

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

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, 
            "q": q, 
            "some_id": f'this is the id #{item_id}'}

@app.post("/items")
async def create_item(item: Item):

    # since it's a brand new item, we associate an item_id to it
    item_id = randint(1,99)
    print(item_id)
    JONS_DB.append(item)

    print('------------ DB (a global var for now) -----------', JONS_DB)
    # the JONS_DB will keep growing... until we kill the server

    return { "message": "201 Successful Creation", 
            "item_name" : item.name, 
            "how much?": item.price,
            "item_id":  item_id,
            "jons_db": JONS_DB
            }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return { "message": "200 Successful update", 
            "item_name" : item.name, 
            "how much?": item.price,
            "item_id": item_id }

@app.post("/postcards", name="Sending postcards cause we love to do so")
async def create_postcard(postcard: PostCard):
    return { "message": "200 Card posted!",
            "payload" : f'On {str(postcard.date)} sent at {postcard.address} text: {postcard.card_body_text} signed: {'xoxo' if postcard.is_signed else 'oops forgot to sign :['}'
            }

@app.post("/uploadfile", name="POSTing binary")
async def create_upload_file(file: UploadFile):
    '''
    #TODO the route doc
    '''
    contents = await file.read()
    return StreamingResponse(
        io.BytesIO(contents),
        media_type='application/octet-stream',
        headers={"Content-Disposition": f"attachment; filename={file.filename}"}
    )

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    i_item_to_remove = find_index_by_id(JONS_DB, item_id)

    if 0 <= i_item_to_remove < len(JONS_DB):
        del JONS_DB[i_item_to_remove]

    return { "message": "204 Successful DELETE", 
            "jons_db": JONS_DB }