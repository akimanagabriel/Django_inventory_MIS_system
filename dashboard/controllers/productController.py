from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import Incoming



@login_required
def index(request):
    return HttpResponse('product index')


@login_required
def create(request):
    return HttpResponse('product create')


@login_required
def store(request):
    return HttpResponse('product store')


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