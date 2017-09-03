import dateutil
import pytest

from pystarling.api_objects.Customer import Customer


class TestCustomer(object):
    test_data = {
        'customerUid': 'b360c371-f8e6-4e28-aca9-37d1d1380176',
        'firstName': 'Anne',
        'lastName': 'Other',
        'dateOfBirth': '1970-02-01',
        'phone': '012345678912',
        'accountHolderType': 'INDIVIDUAL'
    }

    incomplete_data = {
        'firstName': 'Anne',
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Customer(self.incomplete_data)

    def test_data_parsed_correctly(self):
        customer = Customer(self.test_data)
        assert customer.first_name == 'Anne'
        assert customer.last_name == 'Other'
        assert customer.dob == dateutil.parser.parse('1970-02-01')
        assert customer.phone == '012345678912'
        assert customer.customer_uid == 'b360c371-f8e6-4e28-aca9-37d1d1380176'
        assert customer.account_holder_type == "INDIVIDUAL"