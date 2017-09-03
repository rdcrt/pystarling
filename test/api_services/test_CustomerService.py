import os

import dateutil
import responses

from pystarling.api_services.CustomerService import CustomerService


class TestCustomerService(object):
    @responses.activate
    def test_get_customer(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-customers.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}

        responses.add(responses.GET, 'https://starling_base_url/customers', body=file_contents, status=200)

        test_customer_service = CustomerService(config)
        test_customer = test_customer_service.get()

        assert test_customer.customer_uid == '11fee6d4-e121-4833-a7a2-0b9547347e31'
        assert test_customer.first_name == "Anne"
        assert test_customer.last_name == "Other"
        assert test_customer.phone == "01234567890"
        assert test_customer.dob == dateutil.parser.parse("1970-02-21")
        assert test_customer.account_holder_type == "INDIVIDUAL"

