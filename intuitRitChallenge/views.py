from django.shortcuts import render
from intuitRitChallenge.models import *
from django.http import JsonResponse, HttpRequest
from django.core.serializers import serialize
import json


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

        if "account" in request.GET:
            user_id = request.GET["account"]
        else:
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
        if "account" in request.GET:
            user_id = request.GET["account"]
        else:
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

    return JsonResponse(json_data, safe=False)


def not_found(request):
    return render(request, '404_Page.html')
