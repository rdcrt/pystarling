from enum import Enum

import dateutil.parser


class TransactionSource(Enum):
    DIRECT_CREDIT = "Direct Credit"
    DIRECT_DEBIT = "Direct Debit"
    DIRECT_DEBIT_DISPUTE = "Direct Debit Dispute"
    INTERNAL_TRANSFER = "Internal Transfer"
    MASTER_CARD = "MasterCard"
    FASTER_PAYMENTS_IN = "Faster Payments In"
    FASTER_PAYMENTS_OUT = "Faster Payments Out"
    FASTER_PAYMENTS_REVERSAL = "Faster Payments Reversal"
    STRIPE_FUNDING = "Stripe Funding"
    INTEREST_PAYMENT = "Interest Payment"
    NOSTRO_DEPOSIT = "Nostro Deposit"
    OVERDRAFT = "Overdraft"


class TransactionDirection(Enum):
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    NONE = "None"


class BaseTransaction(object):
    def __init__(self, data):
        self.id = data['id']
        self.currency = data['currency']
        self.amount = float(data['amount'])
        self.direction = TransactionDirection[data['direction']]
        self.created = dateutil.parser.parse(data['created'])
        self.narrative = data['narrative']
        self.source = TransactionSource[data['source']]


class SimpleTransaction(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
