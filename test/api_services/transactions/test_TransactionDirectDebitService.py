import os

import dateutil
import responses

from pystarling.api_objects.transactions.BaseTransaction import TransactionDirection, TransactionSource
from pystarling.api_objects.transactions.TransactionDirectDebit import DirectDebitType
from pystarling.api_services.transactions.TransactionDirectDebitService import TransactionDirectDebitService


class TestTransactionDirectDebitService(object):
    @responses.activate
    def test_list_transactions_returns_correct_number_of_transactions(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-directdebit_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/direct-debit', body=file_contents, status=200)

        transaction_direct_debit_service = TransactionDirectDebitService(config)
        test_transaction_list = transaction_direct_debit_service.list()

        assert len(test_transaction_list) == 2

    @responses.activate
    def test_list_transactions_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-directdebit_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/direct-debit', body=file_contents,
                      status=200)

        transaction_direct_debit_service = TransactionDirectDebitService(config)
        test_transaction_list = transaction_direct_debit_service.list()

        assert test_transaction_list[1].id == "038d1ef2-0954-4689-b27e-645bea5a9fab"
        assert test_transaction_list[1].currency == "GBP"
        assert test_transaction_list[1].amount == -130
        assert test_transaction_list[1].direction == TransactionDirection.OUTBOUND
        assert test_transaction_list[1].created == dateutil.parser.parse('2017-05-25T06:42:43.716Z')
        assert test_transaction_list[1].narrative == "Thames Water"
        assert test_transaction_list[1].source == TransactionSource.DIRECT_DEBIT
        assert test_transaction_list[1].mandate_id == 'f54495e2-cd0d-4dda-827b-f3d36e59d69c'
        assert test_transaction_list[1].type == DirectDebitType.DIRECT_DEBIT_FINAL_PAYMENT

    @responses.activate
    def test_single_transaction_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-get-directdebit_transaction.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET,
                      'https://starling_base_url/transactions/direct-debit/03d2ead3-f1fa-4bee-be05-f72bace5db46',
                      body=file_contents, status=200)

        transaction_direct_debit_service = TransactionDirectDebitService(config)
        test_transaction = transaction_direct_debit_service.get("03d2ead3-f1fa-4bee-be05-f72bace5db46")

        assert test_transaction.id == "03d2ead3-f1fa-4bee-be05-f72bace5db46"
        assert test_transaction.currency == "GBP"
        assert test_transaction.amount == 200
        assert test_transaction.direction == TransactionDirection.INBOUND
        assert test_transaction.created == dateutil.parser.parse('2017-08-25T06:42:43.716Z')
        assert test_transaction.narrative == "British Gas"
        assert test_transaction.source == TransactionSource.DIRECT_DEBIT
        assert test_transaction.mandate_id == "e7a8057b-fe04-423c-bf95-c835393ea414"
        assert test_transaction.type == DirectDebitType.FIRST_PAYMENT_OF_DIRECT_DEBIT
