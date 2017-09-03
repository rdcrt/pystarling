from pystarling.api_objects.Addresses import Addresses


class TestAddress(object):
    test_data = {'current': {
        'streetAddress': '123 Fake St',
        'city': 'Springfield',
        'country': 'USA',
        'postcode': 'N1 1AA'
    }, 'previous': {}}

    test_previous_data = {
        'current': {
            'streetAddress': '123 Fake St',
            'city': 'Springfield',
            'country': 'USA',
            'postcode': 'N1 1AA'
        },
        'previous': [
            {
                'streetAddress': '321 Unreal St',
                'city': 'Shelbyville',
                'country': 'USA',
                'postcode': 'S1 9ZZ'
            }
        ]
    }

    def test_addresses_no_previous_gives_empty_array(self):
        addresses = Addresses(self.test_data)
        assert addresses.current.street_address == '123 Fake St'
        assert addresses.current.city == 'Springfield'
        assert addresses.current.country == 'USA'
        assert addresses.current.postcode == 'N1 1AA'

        assert len(addresses.previous) == 0

    def test_addresses_previous_gives_populated_array(self):
        addresses = Addresses(self.test_previous_data)

        assert len(addresses.previous) == 1

        assert addresses.previous[0].street_address == '321 Unreal St'
        assert addresses.previous[0].city == 'Shelbyville'
        assert addresses.previous[0].country == 'USA'
        assert addresses.previous[0].postcode == 'S1 9ZZ'
