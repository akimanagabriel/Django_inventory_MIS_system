from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
]
