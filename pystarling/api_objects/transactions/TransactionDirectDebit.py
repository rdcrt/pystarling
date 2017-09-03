from enum import Enum

from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction


class DirectDebitType(Enum):
    FIRST_PAYMENT_OF_DIRECT_DEBIT = 'First Payment of Direct Debit'
    DEBIT_ROUTING_DATA_MACHINE_READ_FROM_MAGNETIC_STRIP = 'Debit Routing Data Machine Read From Magnetic Strip'
    CLAIM_FOR_UNPAID_CHEQUE = 'Claim for Unpaid Cheque'
    DIRECT_DEBIT = 'Direct Debit'
    DIRECT_DEBIT_REPRESENTATION = 'Direct Debit Representation'
    DIRECT_DEBIT_FINAL_PAYMENT = 'Direct Debit Final Payment'
    INTER_BANK_SETTLEMENT = 'Inter-Bank Settlement'
    BACS_CREDIT = 'BACS Credit'
    CHARGE_TO_CREDIT_CARD = 'Charge to Credit Card'
    REFUND_TO_CREDIT_CARD = 'Refund to Credit Card'
    UNPAID_DIRECT_DEBIT_FIRST_PAYMENT = 'Unpaid Direct Debit First Payment'
    UNPAID_DIRECT_DEBIT = 'Unpaid Direct Debit'
    UNPAID_DIRECT_DEBIT_REPRESENTATION = 'Unpaid Direct Debit Representation'
    UNPAID_DIRECT_DEBIT_FINAL_PAYMENT = 'Unpaid Direct Debit Final Payment'
    BUILDING_SOCIETY_INTEREST_CREDIT = 'Building Society Interest Credit'
    DIVIDENDS_INTEREST = 'Dividends Interest'
    CREDIT_RETURNED_UN_APPLIED = 'Credit Returned UnApplied'


class TransactionDirectDebit(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
        self.mandate_id = data['mandateId']
        self.type = DirectDebitType[data['type']]
