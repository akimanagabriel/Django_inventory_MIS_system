from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    isExpirable = models.BooleanField(default=False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)

class Incoming(models.Model):
    price = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(null=False)
    expirationDate = models.DateField(null=True)
    inDate = models.DateField(default=date.today)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __init__(self, *args, **kwargs):
        super(Incoming, self).__init__(*args, **kwargs)
        self.totalPrice = self.price * self.quantity


class Outgoing(models.Model):
    product = models.ForeignKey(Incoming, on_delete=models.CASCADE)
    outDate = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0)
   
    def __init__(self, *args, **kwargs):
        super(Outgoing, self).__init__(*args, **kwargs)
        self.totalPrice = self.product.price * self.quantity


class Expired(models.Model):
    product = models.ForeignKey(Incoming, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __init__(self, *args, **kwargs):
        super(Expired, self).__init__(*args, **kwargs)
        self.totalPrice = self.product.price * self.quantity