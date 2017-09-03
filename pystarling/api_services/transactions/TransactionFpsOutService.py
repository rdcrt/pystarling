from typing import List

from pystarling.api_objects.transactions.TransactionFpsOut import TransactionFpsOut
from pystarling.api_services.BaseApiService import BaseApiService


class TransactionFpsOutService(BaseApiService):
    ENDPOINT = 'transactions/fps/out'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, transaction_id) -> TransactionFpsOut:
        url = self.ENDPOINT + '/' + transaction_id
        r = self.get_parsed_response(url)
        return TransactionFpsOut(r)

    def list(self, from_date=None, to_date=None) -> List[TransactionFpsOut]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        transactions = r['transactions']
        return [TransactionFpsOut(t) for t in transactions]