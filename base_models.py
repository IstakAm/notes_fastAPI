from pydantic import BaseModel
from typing import Annotated, Union
from fastapi import Query




class User(BaseModel):
    username : str
    password : str


class RegisterUser(User):
    first_name: str
    last_name : str
