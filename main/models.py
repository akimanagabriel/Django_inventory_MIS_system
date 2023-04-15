from datetime import date
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    isExpirable = models.BooleanField(default=False)


class Incoming(models.Model):
    price = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(null=False)
    expirationDate = models.DateField(null=True)
    inDate = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Outgoing(models.Model):
    product = models.ForeignKey(Incoming, on_delete=models.CASCADE)
    outDate = models.DateField(default=date.today)
    quantity = models.IntegerField(null=False)


class Expired(models.Model):
    product = models.ForeignKey(Incoming, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
