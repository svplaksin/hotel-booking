from dataclasses import dataclass
from fastapi import Depends, FastAPI, Query
from typing import Optional
from datetime import date

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)


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
