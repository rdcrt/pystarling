import pytest

from pystarling.api_objects.Address import Address


class TestAddress(object):
    test_data = {
        'streetAddress': '123 Fake St',
        'city': 'Springfield',
        'country': 'USA',
        'postcode': 'N1 1AA'
    }

    incomplete_data = {
        'city': 'Springfield'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Address(self.incomplete_data)

    def test_data_parsed_correctly(self):
        address = Address(self.test_data)
        assert address.street_address == '123 Fake St'
        assert address.city == 'Springfield'
        assert address.country == 'USA'
        assert address.postcode == 'N1 1AA'
