from django.db import models


class Account(models.Model):
    auth_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "User: {}".format(self.auth_id)

    def __repr__(self):
        return self.__str__()


class Transaction(models.Model):
    owner = models.ForeignKey(Account, default=1)
    date = models.DateField()
    vendor = models.CharField(max_length=50, default='None')
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    location = models.CharField(default='None', max_length=2)

    def __str__(self):
        return str(self.owner_auth_id) + ": " + str(self.vendor)


class Features(models.Model):
    owner = models.ForeignKey(Account, default=1)
    salary = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    spending = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    first_top_purchase = models.CharField(default='None', max_length=50)
    second_top_purchase = models.CharField(default='None', max_length=50)
    third_top_purchase = models.CharField(default='None', max_length=50)
