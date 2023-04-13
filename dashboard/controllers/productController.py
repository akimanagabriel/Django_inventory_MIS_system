from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import Category, Incoming
from django.contrib import messages
from datetime import datetime
from main.validation import *
from django.db.models import Q


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
    productPrice = int(request.POST.get('price'))
    productQuantity = int(request.POST.get('quantity'))
    expirationDate = request.POST.get('expiratioDate')

    # validate dates
    if expirationDate:
        expiration = datetime.strptime(expirationDate, '%Y-%m-%d').date()
        now = datetime.now().date()
        days_left = expiration-now

        if days_left.days < 1:
            messages.error(request, "Denied, Your product already expired!")
            return redirect('/dashboard/stock/')

    if productPrice < 5:
        messages.error(request, "product price must start atleast 5RWF")
        return redirect('/dashboard/stock/')

    if productQuantity < 1:
        messages.error(request, "quantity can not be less than 1")
        return redirect('/dashboard/stock/')

    if len(productName) < 3:
        messages.error(
            request, "Product title must be atleast 3 characters long")
        return redirect('/dashboard/stock/')

    existing = Incoming.objects.filter(name=productName)
    if existing:
        messages.error(request, "Product already exist!")
        return redirect("/dashboard/stock/")

    product = Incoming(
        price=productPrice,
        name=productName,
        quantity=productQuantity,
        expirationDate=expirationDate,
        category=Category.objects.filter(id=categoryId)[0]
    )
    product.save()
    messages.success(request, "Product created")
    return redirect('/dashboard/stock/')


@login_required
def show(request, id):
    product = get_object_or_404(Incoming, id=id)
    return render(request,'product/show.html',{
        "product": product,
        "products":Incoming.objects.filter(Q(category=product.category) & ~Q(id=id)).order_by('name'),
        }
    )


@login_required
def edit(request, id):
    return HttpResponse('product edit')


@login_required
def update(request, id):
    return HttpResponse('product update')


@login_required
def destroy(request, id):
    Incoming.objects.filter(id=id).delete()
    messages.success(request, "Product removed successfully!")
    return redirect('/dashboard/stock/')
