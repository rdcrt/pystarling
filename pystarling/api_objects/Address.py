class Address(object):
    def __init__(self, data):
        self.street_address = data['streetAddress']
        self.city = data['city']
        self.country = data['country']
        self.postcode = data['postcode']
