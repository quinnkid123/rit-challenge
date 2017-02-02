from django.shortcuts import render
from intuitRitChallenge import models
from django.http import JsonResponse
from django.core.serializers import serialize


def home_screen(request):
    return render(request, 'index.html', {'view': "dashboard"})


def charts(request):
    return render(request, 'charts.html', {'view': "charts"})


def tables(request):
    transactions = api_transactions(request)
    return render(request, 'tables.html', {'view': "tables", 'data': transactions})


def api_transactions(request):
    transactions = "{'id': \"No data found\"}"
    if request.method == "GET":
        try:
            account = request.GET["account"]
        except KeyError:
            account = ""

        transactions = serialize("json", models.Transaction.objects.filter(owner=account))

    return JsonResponse(transactions)


def not_found(request):
    return render(request, '404_Page.html')
