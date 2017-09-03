from pystarling.api_services import WhoAmIService, BalanceService, AccountService, CustomerService, CardService, \
    AddressService
from pystarling.api_services.transactions import TransactionServiceWrapper

from pystarling.errors import NotAuthorizedError


class StarlingClient(object):
    PRODUCTION_URL = 'https://api.starlingbank.com/api/v1/'

    def __init__(self, auth_token, api_url=PRODUCTION_URL):
        self._config = {'auth_token': auth_token, 'api_url': api_url}

        self.whoami = WhoAmIService.WhoAmIService(self._config)
        self.balance = BalanceService.BalanceService(self._config)
        self.transaction = TransactionServiceWrapper.TransactionServiceWrapper(self._config)
        self.account = AccountService.AccountService(self._config)
        self.customer = CustomerService.CustomerService(self._config)
        self.card = CardService.CardService(self._config)
        self.addresses = AddressService.AddressService(self._config)

        if not self.me().authenticated:
            raise NotAuthorizedError

    def me(self):
        return self.whoami.me()
