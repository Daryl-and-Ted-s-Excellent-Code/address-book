from typing import List
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Boolean, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import databases

CONN_STRING = "postgresql://postgres:password@127.0.0.1:5432/address_book"

engine = create_engine(CONN_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

database = databases.Database(CONN_STRING)
metadata = MetaData()

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    salutation = Column(String)
    is_adult = Column(Boolean, default=False)
    address_id = Column(Integer, ForeignKey("addressentry.id"))
    #address = relationship("AddressEntry", back_populates="people")


class AddressEntry(Base):
    __tablename__ = "addressentry"
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    # residents = relationship(
    #     "Person",
    #     back_populates="address",
    # )

# async def on_startup():
#     await database.connect()


# async def on_shutdown():
#     await database.disconnect()


# engine = create_engine(CONN_STRING)
# metadata.create_all(engine)