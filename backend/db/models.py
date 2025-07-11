from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.sql import func


class TypeBrand(Base):
    __tablename__ = "type_brand_association"

    type_id: Mapped[int] = mapped_column(ForeignKey("types.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[str]

    basket = relationship("Basket", uselist=False, back_populates="user")
    ratings = relationship("Rating", back_populates="user")


class Basket(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    # Связи
    user = relationship("User", back_populates="basket")
    devices = relationship("BasketDevice", back_populates="basket")


class Type(Base):
    name: Mapped[str] = mapped_column(String(150), unique=True)

    # Связи
    brands = relationship(
        "Brand", secondary="type_brand_association", back_populates="types"
    )
    devices = relationship("Device", back_populates="type")


class Brand(Base):
    name: Mapped[str] = mapped_column(String(150), unique=True)

    types = relationship(
        "Type", secondary="type_brand_association", back_populates="brands"
    )
    devices = relationship("Device", back_populates="brand")


class Device(Base):
    name: Mapped[str] = mapped_column(String(150))
    price: Mapped[int]
    rating: Mapped[float | None] = mapped_column(default=0, server_default="0")
    img: Mapped[str | None]
    type_id: Mapped[int] = mapped_column(ForeignKey("types.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))

    # Связи
    type = relationship("Type", back_populates="devices")
    brand = relationship("Brand", back_populates="devices")
    basket_devices = relationship("BasketDevice", back_populates="device")
    ratings = relationship("Rating", back_populates="device")
    info = relationship("DeviceInfo", back_populates="device")


class BasketDevice(Base):

    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))
    basket_id: Mapped[int] = mapped_column(ForeignKey("baskets.id"))

    # Связи
    device = relationship("Device", back_populates="basket_devices")
    basket = relationship("Basket", back_populates="devices")


class Rating(Base):

    rate: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))

    # Связи
    user = relationship("User", back_populates="ratings")
    device = relationship("Device", back_populates="ratings")


class DeviceInfo(Base):

    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(250))
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))

    # Связи
    device = relationship("Device", back_populates="info")
