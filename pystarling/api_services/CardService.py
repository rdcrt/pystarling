from pystarling.api_objects.Card import Card
from pystarling.api_services.BaseApiService import BaseApiService


class CardService(BaseApiService):
    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self) -> Card:
        endpoint = 'cards'
        r = self.get_parsed_response(endpoint)
        return Card(r)
