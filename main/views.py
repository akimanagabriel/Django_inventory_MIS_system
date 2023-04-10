from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

from .validation import *


def landing(request):
    return render(request, 'home.html')


def signup(request):
    # return template if request method is GET
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # validation
        errors = []
        if char_length(request.POST['fname']):
            errors.append("First name must have atleast 3 characters long")
        elif not is_letters_only(request.POST['fname']):
            errors.append("First name must contain characters only")

        if char_length(request.POST['lname']):
            errors.append("Last name must have atleast 3 characters long")
        elif not is_letters_only(request.POST['lname']):
            errors.append("Last name must contain characters only")

        if not is_valid_email(request.POST['email']):
            errors.append("Invalid email address")
            
        if User.objects.filter(email=request.POST['email']):
            errors.append("Email address already exist")

        if char_length(request.POST['username']):
            errors.append("Username must have atleast 3 characters long")

        if len(request.POST['password']) == 0 and len(request.POST['password_confirm']) == 0:
            errors.append('Password can not be empty')
        elif not password_match(request.POST['password'], request.POST['password_confirm']):
            errors.append('Both password must match')

        if len(errors) != 0:
            for err in errors:
                messages.error(request, err)
            del errors
            return redirect('/signup/')

        user = User.objects.create_user(
            request.POST['username'], request.POST['email'], request.POST['password']
        )
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.is_staff = True
        user.save()
        messages.success(
            request, "User created! please login to your account.")
        return redirect('/signin/')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            request.session['userEmail'] = user.email
            request.session['userId'] = user.id
            request.session['username'] = user.username
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid credentials, please try again!")
            return redirect('/signin/')


def signout(request):
    messages.success(request,"You have been logged out")
    logout(request)
    return redirect('/signin/')