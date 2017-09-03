import os

import dateutil
import responses

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_objects.transactions.TransactionMastercard import MasterCardTransactionMethod, \
    MasterCardTransactionStatus
from pystarling.api_services.transactions.TransactionMastercardService import TransactionMastercardService


class TestTransactionSummariesService(object):
    @responses.activate
    def test_list_transactions_returns_correct_number_of_transactions(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-mastercard_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/mastercard', body=file_contents, status=200)

        transaction_summaries_service = TransactionMastercardService(config)
        test_transaction_list = transaction_summaries_service.list()

        assert len(test_transaction_list) == 2

    @responses.activate
    def test_list_transactions_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-mastercard_transactions.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/mastercard', body=file_contents, status=200)

        transaction_mastercard_service = TransactionMastercardService(config)
        test_mastercard_list = transaction_mastercard_service.list()

        assert test_mastercard_list[0].id == "0a35953c-73c2-40d4-a83a-a2ad0c653a70"
        assert test_mastercard_list[0].currency == "GBP"
        assert test_mastercard_list[0].amount == -16.42
        assert test_mastercard_list[0].created == dateutil.parser.parse('2017-08-02T10:55:56.123Z')
        assert test_mastercard_list[0].narrative == "Sainsbury's"
        assert test_mastercard_list[0].source == TransactionSource.MASTER_CARD
        assert test_mastercard_list[0].direction == TransactionDirection.OUTBOUND
        assert test_mastercard_list[0].transaction_method == MasterCardTransactionMethod.CONTACTLESS
        assert test_mastercard_list[0].status == MasterCardTransactionStatus.PENDING
        assert test_mastercard_list[0].source_amount == -16.42
        assert test_mastercard_list[0].source_currency == "GBP"
        assert test_mastercard_list[0].spending_category == "GROCERIES"
        assert test_mastercard_list[0].country == "GBR"

    @responses.activate
    def test_single_transaction_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-get-mastercard_transaction.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET,
                      'https://starling_base_url/transactions/mastercard/1b745b3e-31b5-4f6d-aa80-673557317f32',
                      body=file_contents, status=200)

        transaction_mastercard_service = TransactionMastercardService(config)
        test_transaction_list = transaction_mastercard_service.get('1b745b3e-31b5-4f6d-aa80-673557317f32')

        assert test_transaction_list.id == "1b745b3e-31b5-4f6d-aa80-673557317f32"
        assert test_transaction_list.currency == "GBP"
        assert test_transaction_list.amount == -7.23
        assert test_transaction_list.created == dateutil.parser.parse('2017-07-01T17:53:38.231Z')
        assert test_transaction_list.narrative == "Tesco"
        assert test_transaction_list.source == TransactionSource.MASTER_CARD
        assert test_transaction_list.direction == TransactionDirection.OUTBOUND
        assert test_transaction_list.status == MasterCardTransactionStatus.SETTLED
        assert test_transaction_list.source_amount == -7.23
        assert test_transaction_list.source_currency == "GBP"
        assert test_transaction_list.country == "GBR"
