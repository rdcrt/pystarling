import dateutil.parser


class Account(object):
    def __init__(self, data):
        self.id = data['id']
        self.number = data['number']
        self.sort_code = data['sortCode']
        self.currency = data['currency']
        self.iban = data['iban']
        self.bic = data['bic']
        self.created_at = dateutil.parser.parse(data['createdAt'])

    def get_readable_sort_code(self):
        return "{}-{}-{}".format(self.sort_code[0:2], self.sort_code[2:4], self.sort_code[4:6])

    def get_readable_iban(self):
        return "{} {} {} {} {} {}".format(self.iban[0:4], self.iban[4:8], self.iban[8:12],
                                          self.iban[12:16], self.iban[16:20], self.iban[20:22])
