from pydantic import BaseModel
from typing import Annotated, Union
from fastapi import Query




class user(BaseModel):
    username : str
    first_name : str
    last_name : str
    password : str


class note(BaseModel):
    text : str
    user_id : int

