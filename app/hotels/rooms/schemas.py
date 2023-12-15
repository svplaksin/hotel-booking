from typing import List, Optional
from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int


class SRooomInfo(SRooms):
    total_cost: int
    rooms_left: int
