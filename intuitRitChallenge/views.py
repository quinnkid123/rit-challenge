from django.shortcuts import render
from intuitRitChallenge.models import *
from django.http import JsonResponse
import decimal
import json


def home_screen(request):
    return render(request, 'charts.html', {'view': "charts"})


def charts(request, account=None):
    if account:
        data = api_transactions(request, account)
        return render(request, 'charts.html', {'view': "charts", 'data': data})
    return render(request, 'charts.html', {'view': "charts"})


def tables(request, account=None):
    if account:
        data = json.dumps(get_transactions(account))
        print(data)
        return render(request, 'tables.html', {'view': "tables", 'data': data})
    return render(request, 'tables.html', {'view': "tables"})


def matchmaker(request, account=None, other=None):
    if account and other:
        data = cupid(account, other)
        return render(request, 'matchmaker.html', {'view': "matchmaker", 'data': str(data)})
    return render(request, 'matchmaker.html', {'view': "matchmaker"})


def api_accounts(request):
    json_data = {}
    i = 0
    if request.method == "GET":

        accounts = Accounts.objects.all()
        for account in accounts:
            json_data['account {}'.format(i)] = str(account.auth_id)
            i += 1

    return JsonResponse(json_data)


def api_transactions(request, account):
    json_data = []
    if request.method == "GET":
        json_data = get_transactions(account)

    return JsonResponse(json_data, safe=False)


def get_transactions(account):
    json_data = []
    user_id = account

    transactions = Transactions.objects.filter(owner=user_id)
    for transaction in transactions:
        json_data.append({
            'date': str(transaction.date),
            'vendor': transaction.vendor,
            'amount': str(transaction.amount)
        })

    return json_data


def api_features(request, account):
    json_data = {}
    if request.method == "GET":

        user_id = account

        features = Features.objects.filter(owner=user_id)
        for feature in features:
            json_data = {
                'salary': str(feature.salary),
                'spending': str(feature.spending),
                'first_top_purchase': str(feature.first_top_purchase),
                'second_top_purchase': str(feature.second_top_purchase),
                'third_top_purchase': str(feature.third_top_purchase),
                'has_child': str(feature.has_child),
                'is_sports_fan': str(feature.is_sports_fan),
                'was_recently_divorced': str(feature.was_recently_divorced),
                'favorite_restaurant': str(feature.first_top_purchase)
            }

    return JsonResponse(json_data)


def api_matchmaker(request, account, match):
    json_data = {}
    if request.method == "GET":
        json_data = cupid(account, match)

    return JsonResponse(json_data)


def cupid(soul, mate):
    """
    The ultimate matchmaking algorithm
    :param soul: person 1
    :param mate: person 2
    :return: number between 0 and 1 represent the percentatge match
    """
    # Map all of the user's transactions from vendor to the amount spent there
    soul_transactions = {}
    for transaction in Transactions.objects.filter(owner=soul):
        if transaction.vendor_id.name in soul_transactions:
            soul_transactions[transaction.vendor_id.name] += abs(transaction.amount)
        else:
            soul_transactions[transaction.vendor_id.name] = abs(transaction.amount)

    mate_transactions = {}
    for transaction in Transactions.objects.filter(owner=mate):
        if transaction.vendor_id.name in mate_transactions:
            mate_transactions[transaction.vendor_id.name] += abs(transaction.amount)
        else:
            mate_transactions[transaction.vendor_id.name] = abs(transaction.amount)

    percent_match = decimal.Decimal(0.0)
    count = 0

    # Find all common vendor expense
    for vendor in soul_transactions.keys():
        if vendor in mate_transactions.keys():
            # Determine how similar the amount spent is
            if soul_transactions[vendor] / mate_transactions[vendor] < 1:
                ratio = soul_transactions[vendor] / mate_transactions[vendor]
            else:
                ratio = mate_transactions[vendor] / soul_transactions[vendor]
            # Multiply by the uniqueness of the vendor
            ratio *= decimal.Decimal((101 - Vendors.objects.get(name=vendor).number_of_buyers) / 100)
            percent_match += ratio
            count += 1

    score = percent_match / count  # find the average vendor interest ratio

    json_data = {
        "account": soul,
        "match": mate,
        "score": str(score)
    }

    return json_data


def not_found(request):
    return render(request, '404_Page.html')
