from sqlalchemy import JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]


# This is code for SQLAlchemy v1
# class Hotels(Base):
#     __tablename__ = "hotels"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     services = Column(JSON, nullable=False)
#     rooms_quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)
