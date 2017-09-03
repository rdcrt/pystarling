from pystarling.api_services.BaseApiService import BaseApiService
from pystarling.api_objects.Account import Account


class AccountService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self) -> Account:
        endpoint = 'accounts'
        r = self.get_parsed_response(endpoint)
        return Account(r)

