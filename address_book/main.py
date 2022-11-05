from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from address_book.database import SessionLocal, engine, Base
from address_book.schemas import Address, AddressBase
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


@app.get("/addresses", response_model=list[Address])
def get_all_addresses(db: Session = Depends(get_db)):
    return get_addresses(db)


@app.post("/addresses/", response_model=Address)
def create_new_address(address: AddressBase, db: Session = Depends(get_db)):
    # unique_address = get_unique_address(db, address=address)
    # if unique_address:
    #     raise HTTPException(status_code=400, detail="Address already registered")
    return create_address(db=db, address=address)
