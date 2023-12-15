from datetime import date
from typing import List

from fastapi import APIRouter, Query

from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRooomInfo
# from app.hotels.router import router


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    hotel_id: int,
    date_from: date = Query(...),
    date_to: date = Query(...)
) -> List[SRooomInfo]:
    """
    Описание: возвращает список всех номеров определенного отеля.
Нужно быть авторизованным: нет.
Параметры: параметр пути hotel_id и параметры запроса date_from, date_to.
Ответ пользователю: для каждого номера должно быть указано: id, hotel_id, name,
description, services, price, quantity, image_id, total_cost (стоимость
бронирования номера за весь период), rooms_left (количество оставшихся номеров).
    """
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms
