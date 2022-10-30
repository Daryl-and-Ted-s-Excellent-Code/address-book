from starlite import Starlite

from address_book.controllers.addresses import AddressController

app = Starlite(route_handlers=[AddressController])
