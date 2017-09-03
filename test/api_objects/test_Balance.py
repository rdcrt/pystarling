import pytest

from pystarling.api_objects.Balance import Balance


class TestBalance(object):
    test_data = {
        'amount': 123.45,
        'availableToSpend': 6.78,
        'clearedBalance': 9.02,
        'currency': 'GBP',
        'effectiveBalance': 3.45,
        'pendingTransactions': 6.78
    }

    incomplete_data = {
        'amount': 123.45,
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Balance(self.incomplete_data)

    def test_data_parsed_correctly(self):
        balance = Balance(self.test_data)
        assert balance.amount == 123.45
        assert balance.available_to_spend == 6.78
        assert balance.cleared_balance == 9.02
        assert balance.currency == 'GBP'
        assert balance.effective_balance == 3.45
        assert balance.pending_transactions == 6.78
