from pystarling.api_objects.Address import Address


class Addresses(object):
    def __init__(self, data):
        self.current = Address(data['current'])
        self.previous = [Address(a) for a in data['previous']]
