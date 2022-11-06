from typing import Optional
from sqlalchemy import or_
from sqlalchemy.orm import Session

from . import schemas, models


# region Address


def get_address(db: Session, address_id: int) -> Optional[models.AddressEntry]:
    return (
        db.query(models.AddressEntry)
        .filter(models.AddressEntry.id == address_id)
        .first()
    )


def get_addresses(
    db: Session, keyword: str = None, skip: int = 0, limit: int = 100
) -> Optional[list[models.AddressEntry]]:
    results = db.query(models.AddressEntry).offset(skip).limit(limit).all()
    if keyword:
        results = filter(
            lambda address: keyword.lower() in address["street"].lower(), results
        )

    return results


def create_address(
    db: Session, address: schemas.AddressBase
) -> Optional[models.AddressEntry]:
    db_address = models.AddressEntry(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


# endregion

# region People


def get_people(
    db: Session, keyword: str = None, skip: int = 0, limit: int = 100
) -> Optional[list[models.Person]]:
    if keyword:
        return db.query(models.Person).filter(
            or_(
                models.Person.email.like(keyword),
                models.Person.first_name.like(keyword),
                models.Person.last_name.like(keyword),
            )
        ).all()
    else:
        return db.query(models.Person).offset(skip).limit(limit).all()


def get_person_by_id(db: Session, person_id: int) -> Optional[models.Person]:
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_person_by_email(db: Session, email: str):
    return (
        db.query(models.Person)
        .filter(models.Person.email.lower() == email.lower())
        .first()
    )


def create_person(db: Session, person: schemas.PersonBase) -> Optional[models.Person]:
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def update_person(db: Session, person: schemas.PersonBase) -> Optional[models.Person]:
    db_person = (
        db.query(models.Person).filter(models.Person.id == person.id).one_or_none()
    )
    if db_person is None:
        return None

    # Update model class variable from requested fields
    for var, value in vars(person).items():
        setattr(db_person, var, value) if value else None

    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


# endregion


def update_address_with_person_id(
    db: Session, address_id: int, person_id: int
) -> Optional[models.AddressEntry]:
    db_person = (
        db.query(models.Person).filter(models.Person.id == person_id).one_or_none()
    )
    if db_person is None:
        return None

    setattr(db_person, "address_id", address_id) if address_id >= 0 else None

    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    db_address = get_address(db, address_id)
    return db_address
