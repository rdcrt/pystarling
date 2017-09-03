from typing import List

from pystarling.api_objects.DirectDebitMandate import DirectDebitMandate
from pystarling.api_services.BaseApiService import BaseApiService


class DirectDebitMandateService(BaseApiService):
    ENDPOINT = 'direct-debit/mandates'

    def __init__(self, config):
        BaseApiService.__init__(self, config)

    def get(self, transaction_id) -> DirectDebitMandate:
        url = self.ENDPOINT + '/' + transaction_id
        r = self.get_parsed_response(url)
        return DirectDebitMandate(r)

    def list(self, from_date=None, to_date=None) -> List[DirectDebitMandate]:
        r = self.get_embedded_key_from_parsed_response_with_date_range(self.ENDPOINT, from_date, to_date)
        mandates = r['mandates']
        return [DirectDebitMandate(m) for m in mandates]

