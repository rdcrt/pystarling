import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import TransactionDirection, TransactionSource
from pystarling.api_objects.transactions.TransactionSummary import TransactionSummary


class TestTransactionSummary(object):
    test_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'currency': 'GBP',
        'amount': 12.34,
        'direction': 'OUTBOUND',
        'created': '2017-05-26T12:33:41.723Z',
        'narrative': 'ALDI',
        'source': 'MASTER_CARD',
        'balance': 123.45
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_date_raises_error(self):
        with pytest.raises(KeyError):
            TransactionSummary(self.incomplete_data)

    def test_data_parsed_correctly(self):
        transaction_summary = TransactionSummary(self.test_data)
        assert transaction_summary.id == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert transaction_summary.currency == 'GBP'
        assert transaction_summary.amount == 12.34
        assert transaction_summary.direction == TransactionDirection.OUTBOUND
        assert transaction_summary.created == dateutil.parser.parse('2017-05-26T12:33:41.723Z')
        assert transaction_summary.narrative == 'ALDI'
        assert transaction_summary.source == TransactionSource.MASTER_CARD
        assert transaction_summary.balance == 123.45
