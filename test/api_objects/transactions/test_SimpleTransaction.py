import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import SimpleTransaction, TransactionSource, \
    TransactionDirection


class TestSimpleTransaction(object):
    test_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'currency': 'GBP',
        'amount': 12.34,
        'direction': 'OUTBOUND',
        'created': '2017-05-26T12:33:41.723Z',
        'narrative': 'ALDI',
        'source': 'MASTER_CARD',
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_date_raises_error(self):
        with pytest.raises(KeyError):
            SimpleTransaction(self.incomplete_data)

    def test_data_parsed_correctly(self):
        transaction_summary = SimpleTransaction(self.test_data)
        assert transaction_summary.id == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert transaction_summary.currency == 'GBP'
        assert transaction_summary.amount == 12.34
        assert transaction_summary.direction == TransactionDirection.OUTBOUND
        assert transaction_summary.created == dateutil.parser.parse('2017-05-26T12:33:41.723Z')
        assert transaction_summary.narrative == 'ALDI'
        assert transaction_summary.source == TransactionSource.MASTER_CARD
