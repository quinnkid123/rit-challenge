from django.shortcuts import render
from intuitRitChallenge.models import *
from django.http import JsonResponse, HttpRequest
from django.core.serializers import serialize


def home_screen(request):
    return render(request, 'index.html', {'view': "dashboard"})


def charts(request):
    return render(request, 'charts.html', {'view': "charts"})


def tables(request):
    get_request = HttpRequest()
    get_request.GET = {'account': "72851"}  # TODO don't hard code this
    transactions = api_transactions(get_request)
    return render(request, 'tables.html', {'view': "tables", 'data': transactions})


def api_transactions(request):
    transactions = "{'id': \"No data found\"}"
    if request.method == "GET":
        try:
            account = request.GET["account"]
        except KeyError:
            account = ""

        transactions = Transaction.objects.filter(owner=int(account))
        json = []
        for transaction in transactions:
            json.append({
                'date': transaction.date,
                'vendor': transaction.vendor,
                'amount': transaction.amount
            })

    return transactions


def api_features(request):
    features = "{'id': \"No data found\"}"
    if request.method == "GET":
        try:
            account = request.GET["account"]
        except KeyError:
            account = ""

        features = serialize("json", Features.objects.filter(owner=account))

    return JsonResponse(features)


def not_found(request):
    return render(request, '404_Page.html')
