from typing import Annotated, Union
from fastapi import Cookie, FastAPI
from database.persisting import *
from base_models import *
from utils.password import hash_password
from utils.tokens import generate_token, decode_token
from routers import notes, users


app = FastAPI()

app.include_router(users.router)
app.include_router(notes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


