from typing import List
from pydantic import BaseModel


# region Person


class PersonBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    salutation: str
    is_adult: bool = False


# Properties shared by models stored in DB
class PersonInDBBase(PersonBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Person(PersonInDBBase):
    pass


# endregion

# retion Address


class AddressBase(BaseModel):
    street: str | None = None
    city: str | None = None
    state: str | None = None
    zip_code: str | None = None
    country: str | None = None


# Properties shared by models stored in DB
class AddressInDBBase(AddressBase):
    id: int
    residents: List[PersonBase] = []

    class Config:
        orm_mode = True


# Properties to return to client
class Address(AddressInDBBase):
    pass


# Properties stored in DB
# class AddressInDB(AddressInDBBase):
#     pass


# class AddressEntryCreate(AddressInDBBase):
#     pass

# endregion
