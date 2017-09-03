class Balance(object):
    def __init__(self, data):
        self.amount = float(data['amount'])
        self.available_to_spend = float(data['availableToSpend'])
        self.cleared_balance = float(data['clearedBalance'])
        self.currency = data['currency']
        self.effective_balance = float(data['effectiveBalance'])
        self.pending_transactions = float(data['pendingTransactions'])