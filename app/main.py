from dataclasses import dataclass
from fastapi import Depends, FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


@dataclass
class HotelSearchArgs():
    location: str
    date_from: date
    date_to: date
    has_spa: Optional[bool] = None
    stars: int = Query(None, ge=1, le=5)


@app.get("/hotels")
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass
