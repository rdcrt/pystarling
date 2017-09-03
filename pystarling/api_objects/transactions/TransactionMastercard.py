from enum import Enum

from pystarling.api_objects.transactions.BaseTransaction import BaseTransaction


class MasterCardTransactionMethod(Enum):
    CONTACTLESS = "Contactless"
    MAGNETIC_STRIP = "Magnetic Strip"
    MANUAL_KEY_ENTRY = "Manual Key Entry"
    CHIP_AND_PIN = "Chip and Pin"
    ONLINE = "Online"
    ATM = "ATM"
    APPLE_PAY = "Apple Pay"
    ANDROID_PAY = "Android Pay"
    NOT_APPLICABLE = "N/A"
    UNKNOWN = "Unknown"


class MasterCardTransactionStatus(Enum):
    PENDING = "Pending"
    REVERSED = "Reversed"
    SETTLED = "Settled"
    DECLINED = "Declined"
    CANCELLED = "Cancelled"


class TransactionMasterCard(BaseTransaction):
    def __init__(self, data):
        BaseTransaction.__init__(self, data)
        self.transaction_method = MasterCardTransactionMethod[data['mastercardTransactionMethod']]
        self.status = MasterCardTransactionStatus[data['status']]
        self.source_amount = data['sourceAmount']
        self.source_currency = data['sourceCurrency']
        self.spending_category = data['spendingCategory']
        self.country = data['country'] if 'country' in data else None
