from sqlalchemy.orm import Session

from . import schemas, models


# region Address


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AddressEntry).offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressBase):
    db_address = models.AddressEntry(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


# endregion

# region People


def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.PersonBase):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


# endregion
