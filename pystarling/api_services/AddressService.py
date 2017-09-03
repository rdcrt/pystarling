from pystarling.api_objects.Addresses import Addresses
from pystarling.api_services.BaseApiService import BaseApiService


class AddressService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self) -> Addresses:
        endpoint = 'addresses'
        r = self.get_parsed_response(endpoint)
        return Addresses(r)

