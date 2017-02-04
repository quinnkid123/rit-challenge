"""
The purpose of this script is to identify features based on what the account has purchased.
Although I am only checking for one vendor at a time, I am making the assumption
(based on buyer counts and what I have seen in the transaction data) that similar transaction
categories follow each other.
"""

from intuitRitChallenge.models import Transactions, Accounts, Features, Vendors


def has_purchased_from(vendor_id, account):
    for transaction in Transactions.objects.filter(owner=account):
        if transaction.vendor_id.id == vendor_id:
            return True

    return False


def is_parent(account):
    vendor_id = 43  # Amazon Order - Baby Crib
    return has_purchased_from(vendor_id, account)


def sports_fan(account):
    vendor_id = 11  # NFL Ticket - Chargers
    return has_purchased_from(vendor_id, account)


def divorced(account):
    vendor_id = 33  # Divorce Lawyer Fees
    return has_purchased_from(vendor_id, account)


def top_restaurant(account):
    restaurants = {
        3: 0, 4: 0, 10: 0, 16: 0, 17: 0, 22: 0, 24: 0, 31: 0, 32: 0
    }
    visits = 0
    most_popular = 0
    for transaction in Transactions.objects.filter(owner=account):
        if transaction.vendor_id.id in restaurants.keys():
            restaurants[transaction.vendor_id.id] += 1
            count = restaurants[transaction.vendor_id.id]
            if count > visits:
                visits = count
                most_popular = transaction.vendor_id.id

    if not most_popular:
        print("Not found")
        return None

    return Vendors.objects.filter(id=most_popular)[0]


for user in Accounts.objects.all():
    features = Features.objects.filter(owner=user)[0]
    # features.has_child = is_parent(user)
    # features.is_sports_fan = sports_fan(user)
    # features.was_recently_divorced = divorced(user)
    features.favorite_restaurant = top_restaurant(user).name
    print("Top restaurant: " + str(features.favorite_restaurant))

    features.save()
