"""IntuitChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from intuitRitChallenge import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts', views.api_accounts),  # api/accounts
    url(r'^api/transactions/(?P<account>\d+)', views.api_transactions),  # api/transactions/624
    url(r'^api/features/(?P<account>\d+)', views.api_features),  # api/features/624
    url(r'^api/matchmaker/(?P<account>\d+)/(?P<match>\d+)', views.api_matchmaker),  # api/matchmaker/624/1882
    url(r'^matchmaker/(?P<account>\d+)/(?P<other>\d+)', views.match),  # matchmaker/624/1882
    url(r'^matchmaker', views.match),
    url(r'^charts/(?P<account>\d+)', views.charts),
    url(r'^tables/(?P<account>\d+)', views.tables),
    url(r'^charts', views.charts),
    url(r'^tables', views.tables),
    url(r'^.+', views.not_found),
    url(r'', views.home_screen)

]
