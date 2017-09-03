import pytest

from pystarling.api_objects.Card import Card


class TestCard(object):
    test_data = {
        'id': '9dabc98a-2336-4586-8693-ed092f1b097d',
        'nameOnCard': "A.N. Other",
        'type': 'ContactlessDebitMastercard',
        'enabled': True,
        'cancelled': False,
        'activationRequested': False,
        'activated': True,
        'lastFourDigits': "0001"
    }

    incomplete_data = {
        'id': '9dabc98a-2336-4586-8693-ed092f1b097d',
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Card(self.incomplete_data)

    def test_data_parsed_correctly(self):
        card = Card(self.test_data)
        assert card.id == '9dabc98a-2336-4586-8693-ed092f1b097d'
        assert card.name_on_card == "A.N. Other"
        assert card.enabled
        assert not card.cancelled
        assert not card.activation_requested
        assert card.activated
        assert card.last_four_digits == "0001"
