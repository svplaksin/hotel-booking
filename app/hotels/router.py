from datetime import date
from fastapi import APIRouter
from app.exceptions import HotelsNotFoundException
from app.hotels.dao import HotelsDAO

from app.hotels.schemas import SHotels, SHotelsList


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/{location}")
async def get_hotels_list(
    location: str,
    date_from: date,
    date_to: date
) -> list[SHotelsList]:

    """
    Возвращает список отелей по заданным параметрам,
    причем в отеле должен быть минимум 1 свободный номер.
    Нужно быть авторизованным: нет.
    Параметры: параметр пути location и параметры запроса date_from, date_to.
    Ответ пользователю: для каждого отеля должно быть указано: id, name, location,
    services, rooms_quantity, image_id, rooms_left (количество оставшихся номеров).
    """
    hotels_list = await HotelsDAO.find_all(
        location=location,
        date_from=date_from,
        date_to=date_to
    )
    if not hotels_list:
        raise HotelsNotFoundException
    return hotels_list


@router.get("/id/{hotel_id}")
async def get_one_hotel(hotel_id: int) -> SHotels:
    """
    Описание: возвращает все данные по одному отелю.
    Нужно быть авторизованным: нет.
    Параметры: параметр пути hotel_id.
    """
    return await HotelsDAO.find_one_or_none(id=hotel_id)
