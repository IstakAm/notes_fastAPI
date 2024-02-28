from typing import Annotated, Union
from fastapi import APIRouter, Cookie
from base_models import RegisterUser, User
from database.persisting import create_user, get_user_by_id, verify_user
from utils.password import hash_password
from utils.tokens import decode_token, generate_token


router = APIRouter()



@router.post("/signup")
async def create_user_api(user : RegisterUser):
    user_dict = user.model_dump()
    status = create_user(username=user_dict.get("username"), first_name=user_dict.get("first_name"), last_name=user_dict.get("last_name"), password = hash_password(user_dict.get("password")))
    if status:
        return {"message": "successfully made account"}
    else:
        return {"error": "an error occurred"}
    


@router.post("/login")
async def login_user_api(user : User):
    data = user.model_dump()
    username = data.get("username")
    password = data.get("password")
    user = verify_user(username, password)
    try:
        token = generate_token(user.id)
        return {"message": "signed in", "access_token": token}
    except Exception as e:
        print(e)
        return {"error": "login failed"}


@router.post("/user")
async def get_user_id(access_token: Annotated[Union[str, None], Cookie()] = None):
    payload = decode_token(access_token)
    user_id = payload.get("user_id")
    user = get_user_by_id(user_id)
    return {"username": user.username}