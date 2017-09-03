from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction


class TransactionSummary(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
        self.balance = float(data['balance'])
