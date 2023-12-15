from datetime import date

from sqlalchemy import and_, func, select
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms
from app.dao.base import BaseDAO

from app.database import async_session_maker


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(
        cls,
        hotel_id: int,
        date_from: date,
        date_to: date
    ):
        """
        WITH booked_rooms AS (
            SELECT room_id, COUNT(room_id) AS rooms_booked
            FROM bookings
            WHERE (date_from <= 2023-06-20) AND (date_to >= 2023-15-15)
            FROUP_BY room_id
        )
        SELECT
            -- все столбцы из rooms,
            (quantity - COALESCE(rooms_booked, 0)) AS rooms_left FROM rooms
        LEFT JOIN booked_rooms ON bookedrooms.room_id = rooms.id
        WHERE hotel_id = 1
        """
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id).label("rooms_booked"))
            .select_from(Bookings)
            .where(
                and_(
                    Bookings.date_from <= date_to,
                    Bookings.date_to >= date_from
                )
            )
            .group_by(Bookings.room_id)
            .cte("booked_rooms")
        )

        get_rooms = (
            select(
                Rooms.__table__.columns,
                (Rooms.price * (date_to - date_from).days).label("total_cost"),
                (Rooms.quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)).label("rooms_left"),
            )
            .outerjoin(booked_rooms, booked_rooms.c.room_id == Rooms.id)
            .where(Rooms.hotel_id == hotel_id)
        )

        async with async_session_maker() as session:
            # logger.debug(get_rooms.compile(engine, compile_kwargs={"literal_binds": True}))
            rooms = await session.execute(get_rooms)
            return rooms.mappings().all()
