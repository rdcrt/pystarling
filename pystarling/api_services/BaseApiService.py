import datetime
from typing import Dict

import requests


class BaseApiService(object):
    def __init__(self, config):
        self.auth_token = config['auth_token']
        self.api_url = config['api_url']

    def get_json_response(self, endpoint, params=None):
        request_url = self.api_url + endpoint
        headers = {'Authorization': 'Bearer ' + self.auth_token}
        r = requests.get(request_url, headers=headers, params=params)
        return r

    def get_parsed_response(self, endpoint, params=None):
        raw_response = self.get_json_response(endpoint, params)
        return raw_response.json()

    def get_embedded_key_from_parsed_response(self, endpoint, params=None):
        parsed_response = self.get_parsed_response(endpoint, params=params)
        return parsed_response['_embedded']

    def get_embedded_key_from_parsed_response_with_date_range(self, endpoint, from_date=None, to_date=None):
        params = self.clean_dates(from_date, to_date)
        return self.get_embedded_key_from_parsed_response(endpoint, params)

    @classmethod
    def clean_dates(cls, from_date: str, to_date: str) -> Dict[str, str]:
        if (from_date is not None) and (to_date is None):
            to_date = datetime.date.today().isoformat()
        return {"from": from_date, "to": to_date} if ((from_date and to_date) is not None) else {}
