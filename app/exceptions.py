from typing import Any
from fastapi import HTTPException, status


class BookingException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: Any = ""
    ) -> None:
        super().__init__(status_code, detail)


class UserAlreadyExistsException(HTTPException):
    def __init__(
            self, status_code: int = status.HTTP_409_CONFLICT,
            detail: Any = "Пользователь с таким email уже существует") -> None:
        super().__init__(status_code, detail)


class IncorrectEmailOrPasswordException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Неверно указана почта или пароль"
    ) -> None:
        super().__init__(status_code, detail)


class TokenExpiredException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Срок действия токена истек"
    ) -> None:
        super().__init__(status_code, detail)


class TokenAbsentException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Токен отсутствует"
    ) -> None:
        super().__init__(status_code, detail)


class IncorrectTokenFormatException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Неверный формат токена"
    ) -> None:
        super().__init__(status_code, detail)


class UserMissingException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_401_UNAUTHORIZED
    ) -> None:
        super().__init__(status_code)


class RoomCannotBeBooked(HTTPException):
    def __init__(
            self, status_code: int = status.HTTP_409_CONFLICT,
            detail: Any = "Не осталось свободных номеров") -> None:
        super().__init__(status_code, detail)
