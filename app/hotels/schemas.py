from typing import List, Optional
from pydantic import BaseModel


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int


class SHotelsList(SHotels):
    rooms_left: Optional[int] = None
