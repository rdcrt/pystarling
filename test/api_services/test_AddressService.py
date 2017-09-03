import os

import responses

from pystarling.api_objects import Address
from pystarling.api_services.AddressService import AddressService


class TestAccountServices(object):
    @responses.activate
    def test_get_account_with_previous_parses_correctly(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-list-addresses.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/addresses', body=file_contents, status=200)

        test_address_service = AddressService(config)
        test_addresses = test_address_service.get()

        assert len(test_addresses.previous) == 1

        assert test_addresses.current.street_address == 'Flat 2'
        assert test_addresses.current.city == 'LONDON'
        assert test_addresses.current.country == 'GBR'
        assert test_addresses.current.postcode == 'SW1 1AA'

        assert test_addresses.previous[0].street_address == 'Flat 55'
        assert test_addresses.previous[0].city == 'LONDON'
        assert test_addresses.previous[0].country == 'GBR'
        assert test_addresses.previous[0].postcode == 'NE1 9ZZ'

    @responses.activate
    def test_get_account_with_previous_parses_correctly(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-list-addresses_no_previous.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/addresses', body=file_contents, status=200)

        test_address_service = AddressService(config)
        test_addresses = test_address_service.get()

        assert len(test_addresses.previous) == 0

