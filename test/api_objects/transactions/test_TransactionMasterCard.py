import dateutil
import pytest

from pystarling.api_objects.transactions.BaseTransaction import TransactionSource, TransactionDirection
from pystarling.api_objects.transactions.TransactionMastercard import TransactionMasterCard, MasterCardTransactionMethod


class TestTransactionMasterCard(object):
    test_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'currency': 'GBP',
        'amount': 12.34,
        'direction': 'OUTBOUND',
        'created': '2017-05-26T12:33:41.723Z',
        'narrative': 'ALDI',
        'source': 'MASTER_CARD',
        'mastercardTransactionMethod': 'CONTACTLESS',
        'status': 'SETTLED',
        'sourceAmount':  56.42,
        'sourceCurrency': 'USD',
        'spendingCategory': 'EATING_OUT'
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            TransactionMasterCard(self.incomplete_data)

    def test_data_no_country_parsed_correctly(self):
        transaction_mastercard = TransactionMasterCard(self.test_data)
        assert transaction_mastercard.id == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert transaction_mastercard.currency == 'GBP'
        assert transaction_mastercard.amount == 12.34
        assert transaction_mastercard.direction == TransactionDirection.OUTBOUND
        assert transaction_mastercard.created == dateutil.parser.parse('2017-05-26T12:33:41.723Z')
        assert transaction_mastercard.narrative == 'ALDI'
        assert transaction_mastercard.source == TransactionSource.MASTER_CARD
        assert transaction_mastercard.transaction_method == MasterCardTransactionMethod.CONTACTLESS
        assert transaction_mastercard.status.value == 'Settled'
        assert transaction_mastercard.source_amount == 56.42
        assert transaction_mastercard.source_currency == 'USD'
        assert transaction_mastercard.spending_category == 'EATING_OUT'
        assert transaction_mastercard.country is None

    def test_data_has_country_parsed_correctly(self):
        self.test_data['country'] = 'GBP'
        transaction_mastercard = TransactionMasterCard(self.test_data)
        assert transaction_mastercard.country == 'GBP'
