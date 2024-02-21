from models import *
from connect import engine
from sqlalchemy.orm import Session


session = Session(bind=engine)


def create_user(username, first_name, last_name):
    try:
        user = User(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        session.add(user)
        session.commit()
        return {
            "first_name" : first_name,
            "last_name" : last_name,
            "username" : username
        }
    except Exception as e:
        print(e)
        return ""


def get_user_by_id(user_id):
    user = session.query(User).get(user_id)
    return user

def add_note(text, user):
    try:
        note = Note(text=text)
        note.user = user
        session.add(note)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

