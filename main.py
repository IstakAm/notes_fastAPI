from typing import Annotated, Union
from fastapi import FastAPI, Query
from pydantic import BaseModel
from persisting import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


class user(BaseModel):
    username : Annotated[Union[str, None], Query(max_length=50)] = None
    first_name : Annotated[Union[str, None], Query(max_length=128)] = None
    last_name : Annotated[Union[str, None], Query(max_length=128)] = None



@app.post("/create")
async def create_user_api(user : user):
    user_dict = user.dict()
    status = create_user(username=user_dict.get("username"), first_name=user_dict.get("first_name"), last_name=user_dict.get("last_name"))
    return {"status": status}

class note(BaseModel):
    text : str
    user_id : int


@app.post("/add_note")
async def add_note_api(note_body: note):
    note_dict = note_body.dict()
    user = get_user_by_id(note_dict.get("user_id"))
    status = add_note(note_dict.get("text"), user=user)
    if status :
        return {"message": "made successfully"}
    return {"message": "error occurred"}