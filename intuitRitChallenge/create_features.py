from intuitRitChallenge.models import Accounts, Transaction, Features


def calculate_top_purchases(common_purchases):
    """
    Iterates through a hash table and calculates the top
    three vendors in the hash
    :param common_purchases: a map of vendors to the amount spent there
    :return: top three vendors by name
    """
    first_amount, second_amount, third_amount = 0, 0, 0
    first_vendor, second_vendor, third_vendor = "", "", ""
    for key in common_purchases:

        if common_purchases[key] > third_amount:
            if common_purchases[key] > second_amount:
                if common_purchases[key] > first_amount:
                    first_amount = common_purchases[key]
                    first_vendor = key
                else:
                    second_amount = common_purchases[key]
                    second_vendor = key
            else:
                third_amount = common_purchases[key]
                third_vendor = key

    return first_vendor, second_vendor, third_vendor


def calculate_features(account):
    """
    This function is meant to iterate through the data that has been
    loaded in the database and calculate the more trivia featuers.
    :param account: the account of the user that the features are being generated for
    :return: void
    """
    common_purchases = {}
    income, spending = 0, 0
    for transaction in Transaction.objects.filter(owner=account):
        if transaction.amount > 0:
            income += transaction.amount
        else:
            if transaction.vendor in common_purchases.keys():
                common_purchases[transaction.vendor] += abs(transaction.amount)
            else:
                common_purchases[transaction.vendor] = abs(transaction.amount)
            spending += transaction.amount

    first, second, third = calculate_top_purchases(common_purchases)

    # for income and spending, it is assumed that the data represents two full years of all transactions
    # in the real world, this is unlikely to be true
    feature = Features()
    feature.owner = account
    feature.salary = income / 2
    feature.spending = spending / 2
    feature.first_top_purchase = first
    feature.second_top_purchase = second
    feature.third_top_purchase = third

    feature.save()


def calculate_salary(account):
    """
    This script can be used to just calculate the salaries of the
    accounts in the database
    :param account: a given account in the database
    :return: void
    """
    income, spending = 0, 0
    for transaction in Transaction.objects.filter(owner=account):
        if transaction.amount > 0:
            income += transaction.amount

    feature = Features.objects.filter(owner=account)[0]
    feature.salary = income / 2
    feature.save()


def iterate_all_users():
    """
    Iterate of all of the accounts currently in the database
    :return: void
    """
    for account in Accounts.objects.all():
        print(account)
        calculate_salary(account)


print("Starting script...")
iterate_all_users()
print("Script completed.")
