from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction


class TransactionFpsIn(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
        self.sending_contact_id = data["sendingContactId"] if "sendingContactId" in data else None
        self.sending_contact_account_id = data["sendingContactAccountId"] if "sendingContactAccountId" in data else None
