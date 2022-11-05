from sqlalchemy.orm import Session

from . import schemas, models


def create_address(db: Session, address: schemas.AddressBase):
    db_address = models.AddressEntry(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AddressEntry).offset(skip).limit(limit).all()
