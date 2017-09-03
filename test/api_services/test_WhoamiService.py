import os

import responses

from pystarling.api_services.WhoAmIService import WhoAmIService


class TestWhoAmISerivce(object):
    @responses.activate
    def test_get_whoami(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-whoami.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/me', body=file_contents, status=200)

        test_whoami_service = WhoAmIService(config)
        test_whoami = test_whoami_service.me()

        assert test_whoami.authenticated
        assert test_whoami.customerUid == "49db63e6-dfca-4b57-a243-3856a5e39a17"
        assert test_whoami.expiresInSeconds == 100
        assert test_whoami.scopes == ['account:read', 'balance:read']


