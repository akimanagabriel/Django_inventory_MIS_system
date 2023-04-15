from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import Category, Expired, Incoming, Outgoing
from django.contrib import messages
from datetime import datetime
from main.validation import *
from django.db.models import Q
from datetime import date


@login_required
def index(request):
    expirables = Expired.objects.all().order_by('-id')
    return render(request, 'expired/index.html', {'expirables': expirables})


@login_required
def create(request):
    return HttpResponse('expired create')


@login_required
def store(request):
    return HttpResponse('expired store')


@login_required
def show(request, id):
    return HttpResponse('expired show')


@login_required
def edit(request, id):
    return HttpResponse('expired edit')


@login_required
def update(request, id):
    return HttpResponse('expired update')


@login_required
def destroy(request, id):
    product = get_object_or_404(Expired, id=id).delete()
    messages.success(request, "Product removed successfully!")
    return redirect("/dashboard/expired/")
