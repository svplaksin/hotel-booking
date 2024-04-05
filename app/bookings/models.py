from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import Computed, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.hotels.rooms.models import Rooms
    from app.users.models import Users


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    total_days: Mapped[int] = mapped_column(Computed("(date_to - date_from)"))
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))

    user: Mapped["Users"] = relationship(back_populates="bookings")
    room: Mapped["Rooms"] = relationship(back_populates="bookings")

    def __str__(self) -> str:
        return f"Бронь #{self.id}"

# This is code for SQLAlchemy v1
# class Bookings(Base):
#     __tablename__ = "bookings"

#     id = Column(Integer, primary_key=True)
#     room_id = Column(ForeignKey("rooms.id"))
#     user_id = Column(ForeignKey("users.id"))
#     date_from = Column(Date, nullable=False)
#     date_to = Column(Date, nullable=False)
#     price = Column(Integer, nullable=False)
#     toral_days = Column(Integer, Computed("(date_to - date_from)"))
#     total_cost = Column(Integer, Computed("(date_to - date_from) * price"))

# user = relationship("Users")
# room = relationship("Rooms", back_populates="booking")


# def __str__(self):
#     return f"Бронь #{self.id}"
