from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def index(request, id):
    return render(request, 'user/index.html', {
        "user": get_object_or_404(User, id=id)
    })
