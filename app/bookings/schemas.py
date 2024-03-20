from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_days: int
    total_cost: int
    image_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    services: Optional[List[str]] = None

    class Config:
        from_attributes = True


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
