import os

import dateutil
import responses

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_services.transactions.TransactionFpsOutService import TransactionFpsOutService


class TestTransactionFpsOutService(object):
    @responses.activate
    def test_list_transactions_returns_correct_number_of_transactions(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-fpsout_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/fps/out', body=file_contents, status=200)

        transaction_fpsout_service = TransactionFpsOutService(config)
        test_transaction_list = transaction_fpsout_service.list()

        assert len(test_transaction_list) == 2

    @responses.activate
    def test_list_transactions_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-fpsout_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/fps/out', body=file_contents, status=200)

        transaction_fpsout_service = TransactionFpsOutService(config)
        test_transaction_list = transaction_fpsout_service.list()

        assert test_transaction_list[1].id == "ebd68a81-da63-4b8e-b538-ff2cf3538b2a"
        assert test_transaction_list[1].currency == "GBP"
        assert test_transaction_list[1].amount == -23.45
        assert test_transaction_list[1].direction == TransactionDirection.OUTBOUND
        assert test_transaction_list[1].created == dateutil.parser.parse('2017-08-25T03:36:23.514Z')
        assert test_transaction_list[1].narrative == "More pounds"
        assert test_transaction_list[1].source == TransactionSource.FASTER_PAYMENTS_OUT
        assert test_transaction_list[1].receiving_contact_id is None
        assert test_transaction_list[1].receiving_contact_account_id is None

    @responses.activate
    def test_single_transaction_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-get-fpsout_transaction.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET,
                      'https://starling_base_url/transactions/fps/out/22497667-1416-4119-b2d0-2eef5a322641',
                      body=file_contents, status=200)

        transaction_fpsout_service = TransactionFpsOutService(config)
        test_transaction = transaction_fpsout_service.get("22497667-1416-4119-b2d0-2eef5a322641")

        assert test_transaction.id == "22497667-1416-4119-b2d0-2eef5a322641"
        assert test_transaction.currency == "GBP"
        assert test_transaction.amount == -10
        assert test_transaction.direction == TransactionDirection.OUTBOUND
        assert test_transaction.created == dateutil.parser.parse('2017-08-25T13:56:23.514Z')
        assert test_transaction.narrative == "Extra dollar"
        assert test_transaction.source == TransactionSource.FASTER_PAYMENTS_OUT
        assert test_transaction.receiving_contact_id == "895bac1b-ca48-4701-a281-d3c8c7537a32"
        assert test_transaction.receiving_contact_account_id == "1fae7641-f8f4-4160-8b55-2a7bb40462f5"
