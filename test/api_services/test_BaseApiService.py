from datetime import date

import responses

from pystarling.api_services.BaseApiService import BaseApiService


class TestBaseApiService(object):
    @responses.activate
    def test_clean_dates_returns_empty_both_empty_dates(self):
        from_date = None
        to_date = None

        assert not BaseApiService.clean_dates(from_date, to_date)

    def test_clean_dates_returns_unchanged_dates_if_both_populated(self):
        from_date = "2017-02-05"
        to_date = "2017-03-04"

        assert BaseApiService.clean_dates(from_date, to_date) == {"from": from_date, "to": to_date}

    def test_clean_dates_returns_empty_if_todate_but_not_fromdate(self):
        from_date = None
        to_date = "2017-03-04"

        assert not BaseApiService.clean_dates(from_date, to_date)

    def test_clean_dates_auto_fills_end_with_today_if_todate_but_not_fromdate(self):
        from_date = "2017-03-04"
        to_date = None

        assert BaseApiService.clean_dates(from_date, to_date) == {"from": from_date, "to": date.today().isoformat()}