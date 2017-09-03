from pystarling.api_services.BaseApiService import BaseApiService
from pystarling.api_objects.Whoami import Whoami


class WhoAmIService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def me(self):
        endpoint = 'me'
        r = self.get_parsed_response(endpoint)
        return Whoami(r)

