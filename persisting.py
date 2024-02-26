from models import *
from connect import engine
from sqlalchemy.orm import Session
from password import *

session = Session(bind=engine)


def create_user(username, first_name, last_name, password):
    try:
        user = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
        )
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


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

def verify_user(username, password):
    user = session.query(User).filter(User.username == username).first()
    hashed_pass = user.password
    verify = verify_password(password, hashed_pass)
    if user :
        return user
    return None