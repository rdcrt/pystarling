import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_objects.transactions.TransactionDirectDebit import TransactionDirectDebit, DirectDebitType


class TestTransactionDirectDebit(object):
    test_data = {
        'id': 'f704d00b-bb6c-4a50-96c7-55efceb70119',
        'currency': 'GBP',
        'amount': 456.78,
        'direction': 'OUTBOUND',
        'created': '2017-01-23T12:33:41.747Z',
        'narrative': 'ALDI',
        'source': 'DIRECT_DEBIT',
        'mandateId': '911859bb-05c7-4b0a-a78c-07018d28c65c',
        'type': 'DEBIT_ROUTING_DATA_MACHINE_READ_FROM_MAGNETIC_STRIP'
    }

    incomplete_data = {
        'id': 'f704d00b-bb6c-4a50-96c7-55efceb70119'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            TransactionDirectDebit(self.incomplete_data)

    def test_data_no_country_parsed_correctly(self):
        transaction_direct_debit = TransactionDirectDebit(self.test_data)
        assert transaction_direct_debit.id == 'f704d00b-bb6c-4a50-96c7-55efceb70119'
        assert transaction_direct_debit.currency == 'GBP'
        assert transaction_direct_debit.amount == 456.78
        assert transaction_direct_debit.direction == TransactionDirection.OUTBOUND
        assert transaction_direct_debit.created == dateutil.parser.parse('2017-01-23T12:33:41.747Z')
        assert transaction_direct_debit.narrative == 'ALDI'
        assert transaction_direct_debit.source == TransactionSource.DIRECT_DEBIT
        assert transaction_direct_debit.mandate_id == '911859bb-05c7-4b0a-a78c-07018d28c65c'
        assert transaction_direct_debit.type == DirectDebitType.DEBIT_ROUTING_DATA_MACHINE_READ_FROM_MAGNETIC_STRIP
