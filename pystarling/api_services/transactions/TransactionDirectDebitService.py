from typing import List

from pystarling.api_objects.transactions.TransactionDirectDebit import TransactionDirectDebit
from pystarling.api_services.BaseApiService import BaseApiService


class TransactionDirectDebitService(BaseApiService):
    ENDPOINT = 'transactions/direct-debit'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, transaction_id) -> TransactionDirectDebit:
        url = self.ENDPOINT + '/' + transaction_id
        r = self.get_parsed_response(url)
        return TransactionDirectDebit(r)

    def list(self, from_date=None, to_date=None) -> List[TransactionDirectDebit]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        transactions = r['transactions']
        return [TransactionDirectDebit(t) for t in transactions]

