from pydantic import BaseModel


class AddressEntry(BaseModel):
    first_name: str
    last_name: str