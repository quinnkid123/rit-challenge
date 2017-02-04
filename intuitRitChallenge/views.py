from django.shortcuts import render
from intuitRitChallenge.models import *
from django.http import JsonResponse, HttpRequest
import decimal


def home_screen(request):
    return render(request, 'charts.html', {'view': "charts"})


def charts(request):
    return render(request, 'charts.html', {'view': "charts"})


def tables(request):
    get_request = HttpRequest()
    get_request.GET = {'account': "72851"}  # TODO don't hard code this
    transactions = api_transactions(get_request)
    return render(request, 'tables.html', {'view': "tables", 'data': transactions})


def api_transactions(request, account):
    json_data = []
    if request.method == "GET":

        user_id = account

        transactions = Transactions.objects.filter(owner=user_id)
        for transaction in transactions:
            json_data.append({
                'date': str(transaction.date),
                'vendor': transaction.vendor,
                'amount': str(transaction.amount)
            })

        # json_data = json.dumps(json_data)
    return JsonResponse(json_data, safe=False)


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

    return percent_match / count  # find the average vendor interest ratio


def api_matchmaker(request, account, match):
    json_data = {}
    if request.method == "GET":
        score = cupid(account, match)
        json_data = {
            "account": account,
            "match": match,
            "score": str(score)
        }

    return JsonResponse(json_data)


def not_found(request):
    return render(request, '404_Page.html')
