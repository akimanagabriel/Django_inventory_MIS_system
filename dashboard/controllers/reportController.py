from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import *


@login_required
def index(request):
    return redirect('/dashboard/report/current')

@login_required
def current(request):
    stock_data = Incoming.objects.all().order_by('-inDate')
    return render(request, 'report/current.html',{'current':stock_data})

@login_required
def outgoing(request):
    outgoings = Outgoing.objects.all().order_by('-id')
    return render(request, 'report/outgoing.html',{'outgoings':outgoings})

@login_required
def expired(request):
    expirables = Expired.objects.all().order_by('-id')
    return render(request, 'report/expired.html', {'expirables': expirables})