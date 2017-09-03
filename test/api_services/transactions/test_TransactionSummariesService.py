import os

import dateutil
import responses

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource
from pystarling.api_services.transactions.TransactionSummariesService import TransactionSummariesService


class TestTransactionSummariesService(object):
    @responses.activate
    def test_list_transactions_returns_correct_number_of_transactions(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-transaction_summaries.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions', body=file_contents, status=200)

        transaction_summaries_service = TransactionSummariesService(config)
        test_transaction_list = transaction_summaries_service.list()

        assert len(test_transaction_list) == 3

    @responses.activate
    def test_list_transactions_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-list-transaction_summaries.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions', body=file_contents, status=200)

        transaction_summaries_service = TransactionSummariesService(config)
        test_transaction_list = transaction_summaries_service.list()

        assert test_transaction_list[0].id == "b5c65fd2-1795-4262-93f0-f0490759bf1f"
        assert test_transaction_list[0].currency == "GBP"
        assert test_transaction_list[0].amount == -36.01
        assert test_transaction_list[0].created == dateutil.parser.parse('2017-03-06T12:39:54.936Z')
        assert test_transaction_list[0].narrative == "External Payment"
        assert test_transaction_list[0].source == TransactionSource.FASTER_PAYMENTS_OUT
        assert test_transaction_list[0].balance == 882.39

    @responses.activate
    def test_single_transaction_returns_correct_transaction_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/../responses/v1-get-transaction_summary.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/transactions/dd41b0dc-ed52-4605-b71c-5ab1df1a5547',
                      body=file_contents, status=200)

        transaction_summaries_service = TransactionSummariesService(config)
        test_transaction_list = transaction_summaries_service.get('dd41b0dc-ed52-4605-b71c-5ab1df1a5547')

        assert test_transaction_list.id == "dd41b0dc-ed52-4605-b71c-5ab1df1a5547"
        assert test_transaction_list.currency == "GBP"
        assert test_transaction_list.amount == -5.2
        assert test_transaction_list.created == dateutil.parser.parse('2017-08-20T11:30:13.032Z')
        assert test_transaction_list.narrative == "Argos"
        assert test_transaction_list.source == TransactionSource.MASTER_CARD
