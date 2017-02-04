from intuitRitChallenge.models import Vendors, Accounts, Transactions

for account in Accounts.objects.all():
    purchased_from = set()
    for transaction in Transactions.objects.filter(owner=account):
        purchased_from.add(transaction.vendor_id)

    for vendor in purchased_from:
        row = Vendors.objects.filter(id=vendor.id)[0]
        row.number_of_buyers += 1
        row.save()
