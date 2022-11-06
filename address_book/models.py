from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    email = Column(String, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    salutation = Column(String)
    is_adult = Column(Boolean, default=False)
    address_id = Column(Integer, ForeignKey("addressentry.id"))
    address = relationship("AddressEntry", back_populates="residents")


class AddressEntry(Base):
    __tablename__ = "addressentry"
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    residents = relationship(
        "Person",
        back_populates="address",
    )