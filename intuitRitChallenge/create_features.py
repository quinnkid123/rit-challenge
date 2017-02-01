

from intuitRitChallenge.models import Account, Transaction, Features


def calculate_top_purchases(common_purchases):
    first, second, third = 0, 0, 0
    for key in common_purchases:

        if common_purchases[key] > third:
            if common_purchases[key] > second:
                if common_purchases[key] > first:
                    first = common_purchases[key]
                else:
                    second = common_purchases[key]
            else:
                third = common_purchases[key]

    return first, second, third


def calculate_features(account):
    """
    :param account:
    :return:
    """
    common_purchases = {}
    income, spending = 0, 0
    for transaction in Transaction.objects.filter(owner=account):
        if transaction.amount > 0:
            income += transaction.amount
        else:
            common_purchases[transaction.vendor] += abs(transaction.amount)
            spending += transaction.amount

    first, second, third = calculate_top_purchases(common_purchases)

    # for income and spending, it is assumed that the data represents two full years of all transactions
    # in the real world, this is unlikely to be true
    features = Features()
    features.owner = account
    features.income = income / 2
    features.spending = spending / 2
    features.first_top_purchase = first
    features.second_top_purchase = second
    features.third_top_purchase = third

    features.save()


def iterate_all_users():
    for account in Account.objects.all():
        calculate_features(account)
