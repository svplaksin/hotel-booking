from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr

from app.exceptions import IncorrectEmailOrPasswordException
from app.users.dao import UsersDAO

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.ENCODE_KEY, settings.ENCODE_ALGORITHM
        )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        raise IncorrectEmailOrPasswordException
    return user
