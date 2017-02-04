"""
The purpose of this script is to fill out the foreign key relation from transactions to
the vendors table.

This is done so that each unique vendor can be given an integer key
for abstracting the data into a 3d model for machine learning.
"""

from intuitRitChallenge.models import Transactions, Vendors

vendors_to_pk = {}
i = 1

for transaction in Transactions.objects.all():
    if transaction.vendor not in vendors_to_pk.keys():
        newVendor = Vendors()
        newVendor.id = i
        newVendor.name = transaction.vendor
        transaction.vendor_id = newVendor
        vendors_to_pk[transaction.vendor] = newVendor
        # newVendor.save()
        transaction.save()
        i += 1
    else:
        transaction.vendor_id = vendors_to_pk[transaction.vendor]
        transaction.save()

print("There are {} unique vendors".format(i - 1))
