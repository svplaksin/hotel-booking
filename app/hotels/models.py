from typing import TYPE_CHECKING
from sqlalchemy import JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в
    # PyCharm и VSCode
    from app.hotels.rooms.models import Rooms


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")

    def __str__(self) -> str:
        return f"Отель {self.name} {self.location[:30]}"


# This is code for SQLAlchemy v1
# class Hotels(Base):
#     __tablename__ = "hotels"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     services = Column(JSON, nullable=False)
#     rooms_quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)

# rooms = relationship("Rooms", back_populates="hotel")

# def __str__(self):
#     return f"Отель {self.name} {self.location[:30]}"
