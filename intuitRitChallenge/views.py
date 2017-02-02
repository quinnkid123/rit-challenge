from django.shortcuts import render


def home_screen(request):
    return render(request, 'index.html', {'view': "dashboard"})


def charts(request):
    return render(request, 'charts.html', {'view': "charts"})


def tables(request):
    return render(request, 'tables.html', {'view': "tables"})


def not_found(request):
    return render(request, '404_Page.html')
