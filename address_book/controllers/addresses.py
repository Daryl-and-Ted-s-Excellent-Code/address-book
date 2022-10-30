from starlite import Starlite, get


from typing import List

from pydantic import UUID4
from starlite import Controller, Partial, get, post, put, patch, delete

from address_book.models import AddressEntry


class AddressController(Controller):
    path = "/addresses"

    # @post()
    # async def create_user(self, data: User) -> User:
    #     ...

    @get()
    async def list_addresses(self) -> List[AddressEntry]:
        return [
            AddressEntry(first_name="John", last_name="Doe"),
            AddressEntry(first_name="Jane", last_name="Doe"),
        ]

    # @patch(path="/{user_id:uuid}")
    # async def partial_update_user(self, user_id: UUID4, data: Partial[User]) -> User:
    #     ...

    # @put(path="/{user_id:uuid}")
    # async def update_user(self, user_id: UUID4, data: User) -> User:
    #     ...

    # @get(path="/{user_id:uuid}")
    # async def get_user(self, user_id: UUID4) -> User:
    #     ...

    # @delete(path="/{user_id:uuid}")
    # async def delete_user(self, user_id: UUID4) -> None:
    #     ...
