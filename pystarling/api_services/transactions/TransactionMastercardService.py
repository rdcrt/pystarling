from typing import List

from pystarling.api_objects.transactions.TransactionMastercard import TransactionMasterCard
from pystarling.api_services.BaseApiService import BaseApiService


class TransactionMastercardService(BaseApiService):
    ENDPOINT = 'transactions/mastercard'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, transaction_id) -> TransactionMasterCard:
        url = self.ENDPOINT + '/' + transaction_id
        r = self.get_parsed_response(url)
        return TransactionMasterCard(r)

    def list(self, from_date = None, to_date = None) -> List[TransactionMasterCard]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        transactions = r['transactions']
        return [TransactionMasterCard(t) for t in transactions]


