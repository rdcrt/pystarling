from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction
from pystarling.api_objects.transactions.TransactionSummary import TransactionSummary
from pystarling.api_services.BaseApiService import BaseApiService

from typing import List


class TransactionSummariesService(BaseApiService):
    ENDPOINT = 'transactions'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, id) -> TransactionSummary:
        url = self.ENDPOINT + '/' + id
        r = self.get_parsed_response(url)
        return BaseTransaction(r)

    def list(self, from_date=None, to_date=None) -> List[TransactionSummary]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        transactions = r['transactions']
        return [TransactionSummary(t) for t in transactions]
