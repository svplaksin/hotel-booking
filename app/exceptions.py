from typing import Any
from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)


class UserAlreadyExistsException(HTTPException):
    status_code = status.HTTP_409_CONFLICT,
    detail = "Пользователь с таким email уже существует"


class IncorrectEmailOrPasswordException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверно указана почта или пароль"


class TokenExpiredException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Срок действия токена истек"


class TokenAbsentException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserMissingException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
