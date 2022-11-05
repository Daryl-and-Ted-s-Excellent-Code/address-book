from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

CONN_STRING = "postgresql://postgres:password@127.0.0.1:5432/address_book"

engine = create_engine(CONN_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

database = databases.Database(CONN_STRING)
metadata = MetaData()


