from typing import List

from pystarling.api_objects.transactions.TransactionFpsIn import TransactionFpsIn
from pystarling.api_services.BaseApiService import BaseApiService


class TransactionFpsInService(BaseApiService):
    ENDPOINT = 'transactions/fps/in'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, transaction_id) -> TransactionFpsIn:
        url = self.ENDPOINT + '/' + transaction_id
        r = self.get_parsed_response(url)
        return TransactionFpsIn(r)

    def list(self, from_date=None, to_date=None) -> List[TransactionFpsIn]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        transactions = r['transactions']
        return [TransactionFpsIn(t) for t in transactions]

