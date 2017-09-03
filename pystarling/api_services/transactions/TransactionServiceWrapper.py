from pystarling.api_services.transactions.TransactionDirectDebitService import TransactionDirectDebitService
from pystarling.api_services.transactions.TransactionFpsInService import TransactionFpsInService
from pystarling.api_services.transactions.TransactionFpsOutService import TransactionFpsOutService
from pystarling.api_services.transactions.TransactionMastercardService import TransactionMastercardService
from pystarling.api_services.transactions.TransactionSummariesService import TransactionSummariesService


class TransactionServiceWrapper:
    def __init__(self, config):
        self.summaries = TransactionSummariesService(config)
        self.mastercard = TransactionMastercardService(config)
        self.fps_in = TransactionFpsInService(config)
        self.fps_out = TransactionFpsOutService(config)
        self.direct_debit = TransactionDirectDebitService(config)

