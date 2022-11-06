from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from address_book.database import SessionLocal
from address_book.schemas import (
    Address,
    AddressBase,
    AddressEntryCreate,
    Person,
    PersonBase,
)
from address_book.repository import (
    create_address,
    get_addresses,
    get_people,
    get_person_by_email,
    get_person_by_id,
    create_person,
    update_address_with_person_id,
)


# Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# region Addresses


@app.get("/addresses", status_code=200, response_model=list[Address])
def get_all_addresses(
    db: Session = Depends(get_db),
    keyword: Optional[str] = Query(None, min_length=3, example="123 Sesame St"),
    limit: Optional[int] = 10,
) -> dict:
    return get_addresses(db, keyword, limit)


@app.post("/addresses/", status_code=201, response_model=Address)
def create_new_address(address: AddressBase, db: Session = Depends(get_db)):
    # unique_address = get_unique_address(db, address=address)
    # if unique_address:
    #     raise HTTPException(status_code=400, detail="Address already registered")
    return create_address(db=db, address=address)


# endregion

# region People


@app.get("/people", status_code=200, response_model=list[Person])
def get_all_people(
    db: Session = Depends(get_db),
    keyword: Optional[str] = Query(
        None, min_length=3, example="FirstName or LastName or Email"
    ),
    limit: Optional[int] = 10,
):
    return get_people(db=db, keyword=keyword, limit=limit)


@app.get("/people/{person_id}", status_code=200, response_model=Person)
def read_user(person_id: int, db: Session = Depends(get_db)):
    db_person = get_person_by_id(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_person


@app.post("/people/", status_code=201, response_model=Person)
def create_new_person(person: PersonBase, db: Session = Depends(get_db)):
    # TODO what about shared mailboxes?
    unique_person = get_person_by_email(db, email=person.email)
    if unique_person:
        raise HTTPException(status_code=400, detail="Person already registered")
    return create_person(db=db, person=person)


# endregion


@app.patch(
    "/addresses/{address_id}/person/{person_id}",
    status_code=201,
    response_model=Address,
)
def update_address_with_person(
    address_id: int, person_id: int, db: Session = Depends(get_db)
):
    updated_address = update_address_with_person_id(
        address_id=address_id, person_id=person_id, db=db
    )
    return updated_address
