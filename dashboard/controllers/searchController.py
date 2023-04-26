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
def search(request):
    term = request.GET.get('search')
    if term.isdigit():
        incoming = Incoming.objects.filter(
        Q(name__icontains=term) | Q(price=term) | Q(quantity=term))
    else:
        incoming = Incoming.objects.filter(Q(name__icontains=term))


    return render(request, 'search/results.html', {
        "products": incoming.filter(~Q(quantity=0))
    })
