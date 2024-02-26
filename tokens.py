from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Union
from password import SECRET_KEY


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1, minutes=0),
        'iat': datetime.utcnow(),
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return access_token


