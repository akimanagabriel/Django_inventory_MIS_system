from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Category, Expired, Incoming
from main.validation import *
from django.db.models import Q
from django.contrib import messages
from datetime import datetime


@login_required
def index(request):
    products = Incoming.objects.all()

    for product in products:
        if product.category.isExpirable:
            current_date = datetime.now()
            expiration_date = product.expirationDate
            expiration_datetime = datetime.combine(
                expiration_date, datetime.min.time())
            # check if dates are equal then move to expired
            if expiration_datetime < current_date:
                expired = Expired(product=product, quantity=product.quantity)
                product.quantity = 0
                # validate if already exist in expired
                if Expired.objects.filter(product=product):
                    continue
                expired.save()
                product.save()

    # return HttpResponse(currentDate)
    return render(request, 'stock/stockIndex.html', {'products': products})


@login_required
def categoriesIndex(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'category/categoriesIndex.html', context)


@login_required
def createCategory(request):
    if request.method == 'GET':
        return render(request, 'category/createCategory.html')

    # receive  data from form
    title = str(request.POST.get('title'))
    expireble = bool(request.POST.get('isExpirable'))

    # check if exist
    category = Category.objects.filter(title=title)
    if (category):
        messages.error(request, "Category already exist")
        route = f"/dashboard/category/create/"
        return redirect(route)

    if char_length(title):
        messages.error(
            request, "Category title must be atleast 3 characters long")
        route = f"/dashboard/category/create/"
        return redirect(route)
    if not is_letters_only(title):
        messages.error(request, 'category title must contain characters only')
        route = f"/dashboard/category/create/"
        return redirect(route)

    # insert into db
    category = Category(title=title, isExpirable=expireble, creator=request.user)
    category.save()
    messages.success(request, "category created successfully!")
    return redirect('/dashboard/categories/')


@login_required
def deleleteCategory(request, id):
    Category.objects.filter(id=id).delete()
    messages.success(request, "category removed successfully!")
    return redirect('/dashboard/categories/')


@login_required
def editCategory(request, id):
    context = {'category': Category.objects.filter(id=id)[0]}
    return render(request, 'category/editcategory.html', context)


@login_required
def updateCategory(request, id):
    if char_length(request.POST.get('title')):
        messages.error(
            request, "Category title must be atleast 3 characters long")
        route = f"/dashboard/categories/{id}/edit"
        return redirect(route)
    if not is_letters_only(request.POST.get('title')):
        messages.error(request, 'category title must contain characters only')
        route = f"/dashboard/categories/{id}/edit"
        return redirect(route)

    category = Category.objects.filter(id=id)[0]
    category.title = str(request.POST['title'])
    category.isExpirable = bool(request.POST.get('isExpirable'))
    category.save()
    messages.success(request, "changes saved successfully!")
    return redirect('/dashboard/categories/')


@login_required
def createProduct(request):
    categories = Category.objects.all().order_by('title')
    return render(request, 'stock/createProduct.html', {'categories': categories, 'form': 1})


@login_required
def checkExpirableCategory(request):
    if request.GET.get('category') == None:
        messages.error(request , "You must register category first")
        return redirect('/dashboard/stock/create/')
    
    id = int(request.GET.get('category'))
    category = Category.objects.filter(id=id)[0]
    categories = Category.objects.all().order_by('title')
    return render(request, 'stock/createProduct.html', {'category': category, 'categories': categories, 'form': 2})
