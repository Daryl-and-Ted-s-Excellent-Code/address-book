from sqlalchemy.orm import Session

from . import db, schemas


def create_address(sesh: Session, address: schemas.AddressEntryCreate):
    db_address = db.AddressEntry(**address.dict())
    sesh.add(db_address)
    sesh.commit()
    sesh.refresh(db_address)
    return db_address


def get_addresses(sesh: Session, skip: int = 0, limit: int = 100):
    return sesh.query(db.AddressEntry).offset(skip).limit(limit).all()