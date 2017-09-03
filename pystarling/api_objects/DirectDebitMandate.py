from enum import Enum

import dateutil


class DirectDebitMandateStatus(Enum):
    CANCELLED = "Cancelled"
    LIVE = "Live"


class DirectDebitMandateSource(Enum):
    ELECTRONIC = "Electronic"
    PAPER = "Paper"


class DirectDebitMandate(object):
    def __init__(self, data):
        self.uid = data['uid']
        self.status = DirectDebitMandateStatus[data['status']]
        self.source = DirectDebitMandateSource[data['source']]
        self.reference = data['reference']
        self.originator_uid = data['originatorUid']
        self.originator_name = data['originatorName']
        self.created = dateutil.parser.parse(data['created'])
        self.cancelled = dateutil.parser.parse(data['cancelled']) if 'cancelled' in data else None
