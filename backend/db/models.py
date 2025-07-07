from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.sql import func





class TypeBrand(Base):
    __tablename__ = "type_brand_association"

    type_id:Mapped[int] = mapped_column(ForeignKey('types.id'))
    brand_id:Mapped[int] = mapped_column(ForeignKey('brands.id'))


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[str]
    
    
    basket = relationship("Basket", uselist=False, back_populates="user")
    ratings = relationship("Rating", back_populates="user")


class Basket(Base):
    
    
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Связи
    user = relationship("User", back_populates="basket")
    devices = relationship("BasketDevice", back_populates="basket")


class Type(Base):
    
    name = Column(String, unique=True)
    
    # Связи
    brands = relationship("Brand", secondary="type_brand_association", back_populates="types")
    devices = relationship("Device", back_populates="type")

class Brand(Base):
    name = Column(String, unique=True)
    
    types = relationship("Type", secondary="type_brand_association", back_populates="brands")
    devices = relationship("Device", back_populates="brand")

class Device(Base):
    name = Column(String)
    price = Column(Float)
    rating = Column(Float, default=0.0)
    img = Column(String)
    type_id = Column(Integer, ForeignKey("types.id"))
    brand_id = Column(Integer, ForeignKey("brands.id"))
    
    # Связи
    type = relationship("Type", back_populates="devices")
    brand = relationship("Brand", back_populates="devices")
    basket_devices = relationship("BasketDevice", back_populates="device")
    ratings = relationship("Rating", back_populates="device")
    info = relationship("DeviceInfo", back_populates="device")

class BasketDevice(Base):
    
    device_id = Column(Integer, ForeignKey("devices.id"))
    basket_id = Column(Integer, ForeignKey("baskets.id"))
    
    # Связи
    device = relationship("Device", back_populates="basket_devices")
    basket = relationship("Basket", back_populates="devices")

class Rating(Base):
    
    rate = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    device_id = Column(Integer, ForeignKey("devices.id"))
    
    # Связи
    user = relationship("User", back_populates="ratings")
    device = relationship("Device", back_populates="ratings")

class DeviceInfo(Base):
    
    title = Column(String)
    description = Column(String)
    device_id = Column(Integer, ForeignKey("devices.id"))
    
    # Связи
    device = relationship("Device", back_populates="info")