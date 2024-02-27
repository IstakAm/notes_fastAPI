from passlib.context import CryptContext

SECRET_KEY = "1ZwMfF8lwhDKt+MKJQe/M7rfhnQ8xGqhEL2LM0IGEm3DN/SYI4z57tgd3/IqmV6OccnCjPZ9HdJeoL8t/tiJq0KgILJzplxPequ5tyXpZms="

ALGORITHM = "HS256"

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    return pwd.hash(password)


def verify_password(password, hashed_password):
    return pwd.verify(password, hashed_password)


