import os
from datetime import date, timedelta

from tabulate import tabulate

from pystarling.StarlingClient import StarlingClient


def tabulate_transaction_summary(transaction):
    return [transaction.created.strftime('%d %b %H:%M'),
            transaction.narrative, "{0:.2f}".format(transaction.amount)]


def print_account_details(customer, balance, account, card, addresses):
    print()
    print('Account Name:\t{} {}'.format(customer.first_name, customer.last_name))
    print('Post Code:\t\t{}'.format(addresses.current.postcode))
    print()
    print('Balance:\t\t{}'.format(balance.available_to_spend))
    print()
    print('Account Number:\t{}'.format(account.number))
    print('Sort Code:\t\t{}'.format(account.get_readable_sort_code()))
    print('Card Digits:\t{}'.format(card.last_four_digits))


def print_transaction_summary(transaction_table):
    print()
    print(tabulate(transaction_table, headers=['Date', 'Description', 'Amount']))


if __name__ == "__main__":
    starling_token = os.getenv('STARLING_TOKEN')
    api = StarlingClient(starling_token)
    transaction_start_date = (date.today() - timedelta(weeks=4)).isoformat()

    transactions = api.transaction.summaries.list(transaction_start_date)

    balance = api.balance.get()
    account = api.account.get()
    customer = api.customer.get()
    card = api.card.get()
    addresses = api.addresses.get()

    tabulate_list = [tabulate_transaction_summary(t) for t in transactions]
    print_account_details(customer, balance, account, card, addresses)
    print_transaction_summary(tabulate_list)
