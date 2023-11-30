from datetime import date
from sqlalchemy import Computed, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    toral_days: Mapped[int] = mapped_column(Computed("(date_to - date_from)"))
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))


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
