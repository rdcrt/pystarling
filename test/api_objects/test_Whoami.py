import pytest

from pystarling.api_objects.Whoami import Whoami


class TestWhoAmI(object):
    test_data = {
        'customerUid': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
        'expiresInSeconds': 0,
        'authenticated': True,
        'scopes': ['account:read', 'transaction:read']

    }

    incomplete_data = {
        'customerUid': 'ee8152d7-6ff2-4f79-b9de-39861bdec427',
    }

    def test_incomplete_data_raises_error(self):
        with pytest.raises(KeyError):
            Whoami(self.incomplete_data)

    def test_data_parsed_correctly(self):
        account = Whoami(self.test_data)
        assert account.customerUid == 'ee8152d7-6ff2-4f79-b9de-39861bdec427'
        assert account.expiresInSeconds == 0
        assert account.authenticated
        assert account.scopes == ['account:read', 'transaction:read']
