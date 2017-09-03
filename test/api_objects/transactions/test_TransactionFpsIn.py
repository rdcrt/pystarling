import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_objects.transactions.TransactionFpsIn import TransactionFpsIn


class TestTransactionFpsIn(object):
    test_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'currency': 'GBP',
        'amount': 78.34,
        'direction': 'INBOUND',
        'created': '2017-05-23T12:23:41.723Z',
        'narrative': 'Top Up',
        'source': 'FASTER_PAYMENTS_IN',
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            TransactionFpsIn(self.incomplete_data)

    def test_data_no_contact_info_parsed_correctly(self):
        transaction_fps_in = TransactionFpsIn(self.test_data)
        assert transaction_fps_in.id == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert transaction_fps_in.currency == 'GBP'
        assert transaction_fps_in.amount == 78.34
        assert transaction_fps_in.direction == TransactionDirection.INBOUND
        assert transaction_fps_in.created == dateutil.parser.parse('2017-05-23T12:23:41.723Z')
        assert transaction_fps_in.narrative == 'Top Up'
        assert transaction_fps_in.source == TransactionSource.FASTER_PAYMENTS_IN
        assert transaction_fps_in.sending_contact_id is None
        assert transaction_fps_in.sending_contact_account_id is None

    def test_data_has_country_parsed_correctly(self):
        self.test_data['sendingContactId'] = 'd5de3bc6-5f65-41eb-a414-2331519bcccc'
        self.test_data['sendingContactAccountId'] = 'bd3d17b9-f1dd-4e3a-a897-0dbd8cc22781'
        transaction_fps_in = TransactionFpsIn(self.test_data)
        assert transaction_fps_in.sending_contact_id == 'd5de3bc6-5f65-41eb-a414-2331519bcccc'
        assert transaction_fps_in.sending_contact_account_id == 'bd3d17b9-f1dd-4e3a-a897-0dbd8cc22781'
