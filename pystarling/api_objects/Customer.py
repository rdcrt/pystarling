import dateutil


class Customer(object):
    def __init__(self, data):
        self.customer_uid = data['customerUid']
        self.first_name = data['firstName']
        self.last_name = data['lastName']
        self.dob = dateutil.parser.parse(data['dateOfBirth'])
        self.phone = data['phone']
        self.account_holder_type = data['accountHolderType']
