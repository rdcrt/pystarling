import os

import dateutil
import responses

from pystarling.api_objects.transactions.BaseTransaction import TransactionDirection, TransactionSource
from pystarling.api_services.transactions.TransactionFpsInService import TransactionFpsInService


class TestTransactionsFpsInService(object):
    @responses.activate
    def test_list_transactions_returns_correct_number_of_transactions(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-fpsin_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/fps/in', body=file_contents, status=200)

        transaction_fpsin_service = TransactionFpsInService(config)
        test_transaction_list = transaction_fpsin_service.list()

        assert len(test_transaction_list) == 2

    @responses.activate
    def test_list_transactions_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-fpsin_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/fps/in', body=file_contents, status=200)

        transaction_fpsin_service = TransactionFpsInService(config)
        test_transaction_list = transaction_fpsin_service.list()

        assert test_transaction_list[1].id == "d0692a87-95a1-4f8f-90be-0600fec25c0c"
        assert test_transaction_list[1].currency == "GBP"
        assert test_transaction_list[1].amount == 23.65
        assert test_transaction_list[1].direction == TransactionDirection.INBOUND
        assert test_transaction_list[1].created == dateutil.parser.parse('2017-08-05T22:45:23.594Z')
        assert test_transaction_list[1].narrative == "Bill payment"
        assert test_transaction_list[1].source == TransactionSource.FASTER_PAYMENTS_IN
        assert test_transaction_list[1].sending_contact_id is None
        assert test_transaction_list[1].sending_contact_account_id is None

    @responses.activate
    def test_single_transaction_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-get-fpsin_transaction.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET,
                      'https://starling_base_url/transactions/fps/in/336c1203-a3a8-42ff-b3c0-72228049e6db',
                      body=file_contents, status=200)

        transaction_fpsin_service = TransactionFpsInService(config)
        test_transaction = transaction_fpsin_service.get("336c1203-a3a8-42ff-b3c0-72228049e6db")

        assert test_transaction.id == "336c1203-a3a8-42ff-b3c0-72228049e6db"
        assert test_transaction.currency == "GBP"
        assert test_transaction.amount == 200
        assert test_transaction.direction == TransactionDirection.INBOUND
        assert test_transaction.created == dateutil.parser.parse('2017-08-25T06:42:43.716Z')
        assert test_transaction.narrative == "TOPUP"
        assert test_transaction.source == TransactionSource.FASTER_PAYMENTS_IN
        assert test_transaction.sending_contact_id == "63d8a910-465c-419b-b0e4-f9c843f867dc"
        assert test_transaction.sending_contact_account_id == "74808e7e-8068-429f-9d98-e2a5d48617e9"
