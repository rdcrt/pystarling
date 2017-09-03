from enum import Enum


class CardType(Enum):
    ContactlessDebitMastercard = "Contactless Debit MasterCard"


class Card(object):
    def __init__(self, data):
        self.id = data["id"]
        self.name_on_card = data["nameOnCard"]
        self.card_type = CardType[data["type"]]
        self.enabled = data["enabled"]
        self.cancelled = data["cancelled"]
        self.activation_requested = data["activationRequested"]
        self.activated = data["activated"]
        self.last_four_digits = data["lastFourDigits"]
