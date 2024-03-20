from fastapi import APIRouter, Depends, BackgroundTasks

from pydantic import TypeAdapter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SNewBooking
from app.exceptions import RoomCannotBeBooked, UserMissingException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_current_user_bookings(
    user: Users = Depends(get_current_user)
) -> list[SBooking]:
    return await BookingDAO.get_bookings_list(user_id=user.id)


@router.post("")
async def add_booking(
    background_tasks: BackgroundTasks,
    booking: SNewBooking,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to
    )
    if not booking:
        raise RoomCannotBeBooked
    booking_dict = TypeAdapter(SBooking).validate_python(booking).model_dump()
    # вариант с Celery
    # send_booking_confirmation_email.delay(booking_dict, user.email)
    # вариант со встроенным BackgroundTasks
    background_tasks.add_task(send_booking_confirmation_email, booking_dict, user.email)
    return booking_dict

    booking_dict = TypeAdapter(SBooking).validate_python(booking).model_dump()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict


@router.delete("/{booking_id}")
async def delete_booking(
    booking_id,
    user: Users = Depends(get_current_user),
):
    if not user:
        raise UserMissingException
    else:
        await BookingDAO.delete(booking_id)
