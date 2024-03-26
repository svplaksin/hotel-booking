from typing import TYPE_CHECKING
from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в
    # PyCharm и VSCode
    from app.hotels.models import Hotels
    from app.bookings.models import Bookings


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")
    bookings: Mapped[list["Bookings"]] = relationship(back_populates="room")

    def __str__(self) -> str:
        return f"Номер {self.name}"

# This is code for SQLAlchemy v1
# class Rooms(Base):
#     __tablename__ = "rooms"

#     id = Column(Integer, primary_key=True)
#     hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)
#     services = Column(JSON, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)

    # hotel = relationship("Hotels", back_populates="rooms")
    # bookings = relationship("Bookings", back_populates="room")

    # def __str__(self) -> str:
    #     return f"Номер {self.name}"
