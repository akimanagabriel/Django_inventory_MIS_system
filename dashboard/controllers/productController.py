from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import Category, Incoming
from django.contrib import messages


@login_required
def index(request):
    return HttpResponse('product index')


@login_required
def create(request):
    return HttpResponse('product create')


@login_required
def store(request):
    productName = request.POST.get('productTitle')
    categoryId = request.POST.get('categoryId')
    productPrice = request.POST.get('price')
    productQuantity = request.POST.get('quantity')
    expirationDate = request.POST.get('expiratioDate')

    product = Incoming(
        price=productPrice,
        name=productName,
        quantity=productQuantity,
        expirationDate=expirationDate,
        category=Category.objects.filter(id=categoryId)[0]
    )
    product.save()
    messages.success(request,"Product created")
    return redirect('/dashboard/stock/')


@login_required
def show(request, id):
    return HttpResponse('product show')


@login_required
def edit(request, id):
    return HttpResponse('product edit')


@login_required
def update(request, id):
    return HttpResponse('product update')


@login_required
def destroy(request, id):
    return HttpResponse('product destroy')
