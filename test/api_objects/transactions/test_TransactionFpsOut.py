import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_objects.transactions.TransactionFpsOut import TransactionFpsOut


class TestTransactionFpsOut(object):
    test_data = {
        'id': 'e06641940-6fa4-4d8a-9877-4d9d614f03a4',
        'currency': 'GBP',
        'amount': 99.12,
        'direction': 'OUTBOUND',
        'created': '2017-04-23T12:23:41.723Z',
        'narrative': 'Top Up',
        'source': 'FASTER_PAYMENTS_OUT',
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            TransactionFpsOut(self.incomplete_data)

    def test_data_no_contact_info_parsed_correctly(self):
        transaction_fps_out = TransactionFpsOut(self.test_data)
        assert transaction_fps_out.id == 'e06641940-6fa4-4d8a-9877-4d9d614f03a4'
        assert transaction_fps_out.currency == 'GBP'
        assert transaction_fps_out.amount == 99.12
        assert transaction_fps_out.direction == TransactionDirection.OUTBOUND
        assert transaction_fps_out.created == dateutil.parser.parse('2017-04-23T12:23:41.723Z')
        assert transaction_fps_out.narrative == 'Top Up'
        assert transaction_fps_out.source == TransactionSource.FASTER_PAYMENTS_OUT
        assert transaction_fps_out.receiving_contact_id is None
        assert transaction_fps_out.receiving_contact_account_id is None

