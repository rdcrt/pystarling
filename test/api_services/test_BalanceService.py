import os

import responses

from pystarling.api_services.BalanceService import BalanceService


class TestBalanceSerice(object):
    @responses.activate
    def test_get_balance(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-balance.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/accounts/balance', body=file_contents, status=200)

        test_balance_service = BalanceService(config)
        test_balance = test_balance_service.get()

        assert test_balance.amount == 419.21
        assert test_balance.cleared_balance == 104.50
        assert test_balance.pending_transactions == 32.04
        assert test_balance.available_to_spend == 310.12
        assert test_balance.currency == 'GBP'
        assert test_balance.effective_balance == 423.11

