import os

import dateutil
import responses

from pystarling.api_services.AccountService import AccountService


class TestAccountServices(object):
    @responses.activate
    def test_get_account(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-accounts.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/accounts', body=file_contents, status=200)

        test_account_service = AccountService(config)
        test_account = test_account_service.get()

        assert test_account.id == '49db63e6-dfca-4b57-a243-3856a5e39a17'
        assert test_account.sort_code == '608371'
        assert test_account.number == '99999999'
        assert test_account.iban == 'GB26SRLG60837199999999'
        assert test_account.bic == 'SRLGGB2L'
        assert test_account.currency == 'GBP'
        assert test_account.created_at == dateutil.parser.parse('2017-05-16T12:00:00.000Z')

