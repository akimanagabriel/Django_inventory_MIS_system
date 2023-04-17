from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login

@login_required
def index(request):
    user = request.user
    return render(request, 'setting/index.html', {'user': user})

@login_required
def updateUser(request,id):
    # get data from form
    username = request.POST.get('username')
    email = request.POST.get('email')
    fname = request.POST.get('fn')
    lname = request.POST.get('ln')
    
    user = get_object_or_404(User,id=id)
    user.username = username
    user.first_name = fname
    user.last_name = lname
    user.email = email
    user.save()
    # update session data
    request.session['userEmail'] = user.email
    request.session['userId'] = user.id
    request.session['username'] = user.username
    # set message
    messages.success(request, "changes saved successfully")
    return redirect("/dashboard/setting/")

@login_required
def changePassword(request,id):
    oldPassword = request.POST.get('old')
    newPassword = request.POST.get('new')
    comfirmation = request.POST.get('comfirm')
    
    if not newPassword == comfirmation:
        messages.error(request,"New password and comfirmatiom must match")
        return redirect("/dashboard/setting/")
    if len(comfirmation) < 5:
        messages.error(request,"password must be atleast 5 characters long")
        return redirect("/dashboard/setting/")
    
    user = authenticate(request,username = request.user.username,password = oldPassword)
    if user is not None:
        # update user's password
        hashed = make_password(newPassword)
        user.set_password(hashed)
        user.save()
        # update session data
        request.session['userEmail'] = user.email
        request.session['userId'] = user.id
        request.session['username'] = user.username
        login(request,user)
        messages.success(request,"Password changed successfully!")
        return redirect("/dashboard/setting/")
    else:
        messages.error(request,"You must provide a correct current password")
        return redirect("/dashboard/setting/")
    