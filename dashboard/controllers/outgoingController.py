from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import Category, Incoming, Outgoing
from django.contrib import messages
from datetime import datetime
from main.validation import *
from django.db.models import Q
from datetime import date


@login_required
def index(request):
    outProducts = Outgoing.objects.all().order_by('-id')
    return render(request, 'outgoing/index.html', {"outgoings": outProducts})


@login_required
def create(request):
    return HttpResponse('outgoing create')


@login_required
def store(request):
    return HttpResponse('outgoing store')


@login_required
def show(request, id):
    return HttpResponse('outgoing show')


@login_required
def edit(request, id):
    return HttpResponse('outgoing edit')


@login_required
def update(request, id):
    return HttpResponse('outgoing update')


@login_required
def destroy(request, id):
    product = get_object_or_404(Outgoing, id=id).delete()
    messages.success(request, "Product removed successfully!")
    return redirect("/dashboard/outgoing/")
