from typing import Annotated, Union
from fastapi import APIRouter, Cookie

from database.persisting import add_note, delete_note, get_note_by_id, get_user_by_id, get_user_notes
from utils.serializers import notes_serializer
from utils.tokens import decode_token


router = APIRouter()



@router.post("/add_note")
async def add_note_api(note : str, access_token: Annotated[Union[str, None], Cookie()] = None):
    user = get_user_by_id(decode_token(access_token).get("user_id"))
    status = add_note(note, user=user)
    if status :
        return {"message": "made successfully"}
    return {"message": "error occurred"}


@router.get("/notes")
async def user_notes_api(access_token: Annotated[Union[str, None], Cookie()] = None):
    user_id = decode_token(access_token).get("user_id")
    return {"data": notes_serializer(get_user_notes(user_id))}


@router.delete("/delete_note")
async def delete_note_api(note_id : int, access_token: Annotated[Union[str, None], Cookie()] = None):
    user = get_user_by_id(decode_token(access_token).get("user_id"))
    note = get_note_by_id(note_id)
    if note.user == user:
        status = delete_note(note_id)
        if status:
            return {"message": "deleted"}
        return {"error": "an error occurred"}
    return {"message": "note not found"}