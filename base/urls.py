from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/', lambda arg: redirect('/signin/')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('main.urls'))
]
