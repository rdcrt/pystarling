import dateutil
import pytest

from pystarling.api_objects.DirectDebitMandate import DirectDebitMandate, DirectDebitMandateStatus, \
    DirectDebitMandateSource


class TestDirectDebitMandate(object):
    test_data = {
        "cancelled": "2015-01-06T12:23:08.369Z",
        "created": "2015-01-12T21:42:34.472Z",
        "originatorName": "AN OTHER",
        "originatorUid": "7d980534-7d98-0534-7d98-05347d980534",
        "reference": "text",
        "source": "ELECTRONIC",
        "status": "CANCELLED",
        "uid": "0001c450-0001-c450-0001-c4500001c450"
    }

    incomplete_data = {
        'id': '0001c450-0001-c450-0001-c4500001c450',
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            DirectDebitMandate(self.incomplete_data)

    def test_data_parsed_correctly(self):
        direct_debit = DirectDebitMandate(self.test_data)
        assert direct_debit.uid == '0001c450-0001-c450-0001-c4500001c450'
        assert direct_debit.originator_name == 'AN OTHER'
        assert direct_debit.originator_uid == '7d980534-7d98-0534-7d98-05347d980534'
        assert direct_debit.status == DirectDebitMandateStatus.CANCELLED
        assert direct_debit.source == DirectDebitMandateSource.ELECTRONIC
        assert direct_debit.reference == 'text'
        assert direct_debit.created == dateutil.parser.parse("2015-01-12T21:42:34.472Z")
        assert direct_debit.cancelled == dateutil.parser.parse("2015-01-06T12:23:08.369Z")