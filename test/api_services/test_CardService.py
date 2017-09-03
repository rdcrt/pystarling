import os

import responses

from pystarling.api_objects.Card import CardType
from pystarling.api_services.CardService import CardService


class TestCardService(object):
    @responses.activate
    def test_get_balance(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-card.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/cards', body=file_contents, status=200)

        test_card_service = CardService(config)
        test_card = test_card_service.get()

        assert test_card.id == "1fb03098-5fdd-4464-93b9-b8fa7e26f697"
        assert test_card.name_on_card == "A.N. Other"
        assert test_card.card_type == CardType.ContactlessDebitMastercard
        assert test_card.enabled
        assert not test_card.cancelled
        assert test_card.activation_requested
        assert test_card.activated
        assert test_card.last_four_digits == "0001"

