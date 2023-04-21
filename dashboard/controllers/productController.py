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
        if existing[0].quantity == 0:
            existing[0].name = "exported#"+productName
            existing[0].save()
        elif existing[0].quantity == 0:
            messages.error(request, 'Product already exist')
            return redirect('/dashboard/stock/')

    product = Incoming(
        price=productPrice,
        name=productName,
        quantity=productQuantity,
        expirationDate=expirationDate,
        category=Category.objects.filter(id=categoryId)[0],
        creator=request.user
    )
    product.save()
    messages.success(request, "Product created")
    return redirect('/dashboard/stock/')


@login_required
def show(request, id):
    product = get_object_or_404(Incoming, id=id)
    return render(request, 'product/show.html', {
        "product": product,
        "products": Incoming.objects.filter(Q(category=product.category) & ~Q(id=id)).order_by('name'),
        "categories": Category.objects.filter(Q(isExpirable=product.category.isExpirable))
    }
    )


@login_required
def edit(request, id):
    return HttpResponse('product edit')


@login_required
def update(request, id):
    product = get_object_or_404(Incoming, id=id)
    category_id = int(request.POST.get('category'))
    category = Category.objects.filter(id=category_id)[0]
    product.name = request.POST.get('name')
    product.price = request.POST.get('price')
    product.quantity = request.POST.get('quantity')
    product.category = category
    product.save()

    route = f"/dashboard/product/{id}/show"
    messages.success(request, "Product updated")
    return redirect(route)


@login_required
def destroy(request, id):
    product = get_object_or_404(Incoming, id=id)
    product.quantity = 0
    product.save()
    messages.success(request, "Product removed successfully!")
    return redirect('/dashboard/stock/')


@login_required
def export(request, id):
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Incoming, id=id)
    existOutgoingProduct = Outgoing.objects.filter(product=product)

    # validate qty
    if quantity > product.quantity:
        messages.error(
            request, f"Quantity must be less or equal to {product.quantity}")
        return redirect(f"/dashboard/product/{product.id}/show")

    elif quantity < 1:
        messages.error(request, f"Quantity must be greater than 0")
        return redirect(f"/dashboard/product/{product.id}/show")

    else:
        remainQuantity = product.quantity - quantity
        product.quantity = remainQuantity
        product.save()

        if existOutgoingProduct:
            existOutgoingProduct[0].quantity += quantity
            existOutgoingProduct[0].outDate = str(date.today())
            existOutgoingProduct[0].save()
        else:
            outgoing = Outgoing(quantity=quantity, product=product)
            outgoing.save()

        messages.success(request, f"{product.name} product exported!")
        return redirect("/dashboard/stock/")


@login_required
def allByCatId(request, id: int):
    category = get_object_or_404(Category, id=id)
    products = Incoming.objects.filter(Q(category=category))
    return render(request, 'stock/stockIndex.html', {'products': products})
