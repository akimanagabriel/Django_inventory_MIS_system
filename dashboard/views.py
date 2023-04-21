
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Category, Incoming, Outgoing, Expired
from django.db.models import Q,Sum


@login_required
def home(request):
    # counts of all models
    incomingCount = Incoming.objects.filter(~Q(quantity=0)).count()
    expiredCount = Expired.objects.filter(~Q(quantity=0)).count()
    outgoingCount = Outgoing.objects.count()

    # total of all models' price*quantity
    incoming_prices = []
    for p in Incoming.objects.all():
        result = int(p.price*p.quantity)
        incoming_prices.append(result)
    incoming_total = sum(incoming_prices)

    outgoing_prices = []
    for p in Outgoing.objects.all():
        result = int(p.product.price*p.quantity)
        outgoing_prices.append(result)
    outgoing_total = sum(outgoing_prices)

    expired_prices = []
    for p in Expired.objects.all():
        result = int(p.product.price*p.quantity)
        expired_prices.append(result)
    expired_total = sum(expired_prices)

    # price of all models
    incoming_qty = Incoming.objects.aggregate(Sum('quantity'))['quantity__sum']
    outgoing_qty = Outgoing.objects.aggregate(Sum('quantity'))['quantity__sum']
    expired_qty = Expired.objects.aggregate(Sum('quantity'))['quantity__sum']
   
    #-------------CATEGORIES-------------- # 
    # registered category data
    products = Incoming.objects.filter(~Q(quantity=0))
    categories_list = set()
    for product in products:
        categories_list.add(product.category.title)
    
    # find number of records found in every categories
    products_count_by_category = []
    for category_name in categories_list:
        category = Category.objects.filter(title=category_name)[0]
        count = Incoming.objects.filter(Q(category=category)& ~Q(quantity=0)).count()
        products_count_by_category.append(count)
    
    # latest products
    latest_products = Incoming.objects.filter(~Q(quantity=0)).order_by('-id')
    
    context = {
        "incoming_count": incomingCount,
        "outgoing_count": outgoingCount,
        "expired_count": expiredCount,

        "expired_price": expired_total,
        "outgoing_price": outgoing_total,
        "incoming_price": incoming_total,
        
        "incoming_quantity": incoming_qty,
        "outgoing_quantity": outgoing_qty,
        "expired_quantity":expired_qty,
        
        "categories_list":categories_list,
        "products_in_category": products_count_by_category,
        "latest_products":latest_products[:3]
    }
    return render(request, 'dashboard/index.html', context)
