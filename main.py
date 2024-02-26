from typing import Annotated, Union
from fastapi import FastAPI, Query
from pydantic import BaseModel
from persisting import *
from base_models import *
from password import hash_password
from tokens import generate_token


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}




@app.post("/signup")
async def create_user_api(user : user):
    user_dict = user.dict()
    status = create_user(username=user_dict.get("username"), first_name=user_dict.get("first_name"), last_name=user_dict.get("last_name"), password = hash_password(user_dict.get("password")))
    if status:
        return {"message": "successfully made account"}
    else:
        return {"error": "an error occurred"}
    
@app.post("/login")
async def login_user_api(user : user):
    data = user.dict()
    username = data.get("username")
    password = data.get("password")
    user = verify_user(username, hash_password(password))
    if user:
        token = generate_token(user.id)
        return {"message": "signed in", "access_token": token}
    return {"error": "login failed"}


@app.post("/add_note")
async def add_note_api(note_body: note):
    note_dict = note_body.dict()
    user = get_user_by_id(note_dict.get("user_id"))
    status = add_note(note_dict.get("text"), user=user)
    if status :
        return {"message": "made successfully"}
    return {"message": "error occurred"}