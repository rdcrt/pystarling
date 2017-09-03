from pystarling.api_services.BaseApiService import BaseApiService
from pystarling.api_objects.Balance import Balance


class BalanceService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self) -> Balance:
        endpoint = 'accounts/balance'
        r = self.get_parsed_response(endpoint)
        return Balance(r)
