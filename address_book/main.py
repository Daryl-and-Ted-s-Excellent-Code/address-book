from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from address_book.database import SessionLocal, engine, Base
from address_book.schemas import Address, AddressBase, Person, PersonBase
from address_book.repository import (
    create_address,
    get_addresses,
    get_people,
    create_person,
)


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# region Addresses


@app.get("/addresses", response_model=list[Address])
def get_all_addresses(db: Session = Depends(get_db)):
    return get_addresses(db)


@app.post("/addresses/", response_model=Address)
def create_new_address(address: AddressBase, db: Session = Depends(get_db)):
    # unique_address = get_unique_address(db, address=address)
    # if unique_address:
    #     raise HTTPException(status_code=400, detail="Address already registered")
    return create_address(db=db, address=address)


# endregion

# region People


@app.get("/people", response_model=list[Person])
def get_all_people(db: Session = Depends(get_db)):
    return get_people(db)


@app.post("/people/", response_model=Person)
def create_new_person(person: PersonBase, db: Session = Depends(get_db)):
    # unique_person = get_person_by_email(db, person=person)
    # if unique_person:
    #     raise HTTPException(status_code=400, detail="Person already registered")
    return create_person(db=db, person=person)


# endregion
