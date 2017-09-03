import dateutil
import pytest

from pystarling.api_objects.Account import Account


class TestAccount(object):
    test_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'number': '99999999',
        'sortCode': '608371',
        'iban': 'GB26SRLG60837199999999',
        'bic': 'SRLGGB2L',
        'currency': 'GBP',
        'createdAt': '2017-05-16T12:00:00.000Z'
    }

    incomplete_data = {
        'id': 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Account(self.incomplete_data)

    def test_data_parsed_correctly(self):
        account = Account(self.test_data)
        assert account.id == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert account.sort_code == '608371'
        assert account.number == '99999999'
        assert account.iban == 'GB26SRLG60837199999999'
        assert account.bic == 'SRLGGB2L'
        assert account.currency == 'GBP'
        assert account.created_at == dateutil.parser.parse('2017-05-16T12:00:00.000Z')

    def test_get_readable_sort_code_formatted_correctly(self):
        account = Account(self.test_data)
        assert account.get_readable_sort_code() == '60-83-71'

    def test_get_readable_iban_formatted_correctly(self):
        account = Account(self.test_data)
        assert account.get_readable_iban() == "GB26 SRLG 6083 7199 9999 99"
