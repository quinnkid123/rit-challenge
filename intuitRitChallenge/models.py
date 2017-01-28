from django.db import models
from django.utils import timezone


# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(Account)
    date = models.DateField()
    vendor = models.CharField(default='None')
    amount = models.DecimalField(default=0)
    location = models.CharField(default='None')


class Account(models.Model):
    transactions = models.ForeignKey(Transaction)
    auth_id = models.IntegerField(primary_key=True)


class Features(models.Model):
    income = models.DecimalField(default=0)
    common_purchases = models.CharField(default='None')
    spending = models.DecimalField()
