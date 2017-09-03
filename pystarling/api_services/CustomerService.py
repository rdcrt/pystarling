from pystarling.api_services.BaseApiService import BaseApiService
from pystarling.api_objects.Customer import Customer


class CustomerService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self) -> Customer:
        endpoint = 'customers'
        r = self.get_parsed_response(endpoint)
        return Customer(r)
