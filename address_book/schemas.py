from typing import List
from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    salutation: str
    is_adult: bool = False


class AddressBase(BaseModel):
    street: str | None = None
    city: str | None = None
    state: str | None = None
    zip_code: str | None = None
    country: str | None = None


class AddressEntry(AddressBase):
    id: int = 0
    residents: List[Person] = []

    class Config:
        orm_mode = True


class AddressEntryCreate(AddressEntry):
    pass