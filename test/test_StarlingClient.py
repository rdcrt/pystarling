import os

import pytest
import responses

from pystarling.StarlingClient import StarlingClient
from pystarling.errors import NotAuthorizedError


class TestWhoAmISerivce(object):
    @responses.activate
    def test_client_raises_error_if_not_authf(self):
        with pytest.raises(NotAuthorizedError):
            test_file = os.path.dirname(os.path.realpath(__file__)) + '/api_services/responses/v1-get-whoami_not_authd.json'
            file_contents = open(test_file, 'r').read()
            responses.add(responses.GET, 'https://starling_base_url/me', body=file_contents, status=200)

            StarlingClient('stub', api_url='https://starling_base_url/')


