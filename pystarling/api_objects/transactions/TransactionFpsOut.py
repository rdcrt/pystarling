from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction


class TransactionFpsOut(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
        self.receiving_contact_id = data["receivingContactId"] if "receivingContactId" in data else None
        self.receiving_contact_account_id = data["receivingContactAccountId"] if "receivingContactAccountId" in data else None

