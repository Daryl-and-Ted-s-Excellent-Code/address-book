# from address_book.db import on_startup, on_shutdown
from sqlalchemy.ext.asyncio import AsyncSession
#from address_book.controllers.addresses import AddressController
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from address_book.db import SessionLocal, database, engine, Base
from address_book.schemas import AddressEntry
from address_book.repository import create_address, get_addresses

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

@app.get("/addresses", response_model=AddressEntry)
def get_all_addresses(db: Session = Depends(get_db)):
    return get_addresses(db)


@app.post("/addresses", response_model=AddressEntry)
async def create_address(request: AddressEntry):
    pass
