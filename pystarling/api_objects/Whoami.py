
class Whoami(object):
    def __init__(self, data):
        self.customerUid = data['customerUid']
        self.authenticated = data['authenticated']
        self.expiresInSeconds = int(data['expiresInSeconds'])
        self.scopes = data['scopes']