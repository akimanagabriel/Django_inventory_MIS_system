from datetime import date
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    isExpirable = models.BooleanField(default=False)


class Incoming(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    expirationDate = models.DateField(null=True)
    inDate = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Outgoing(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    outDate = models.DateField(default=date.today)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expirationDate = models.DateField(null=True)


class Expired(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expirationDate = models.DateField(null=True)
