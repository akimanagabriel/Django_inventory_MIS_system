from django.urls import path
from . import views
from .controllers import stockController

urlpatterns = [
    path('', views.home),
    path('stock/', stockController.index),
    path('stock/create/', stockController.createProduct),
    path('categories/',stockController.categoriesIndex),
    path('category/create/',stockController.createCategory),
    path('categories/<int:id>/delete',stockController.deleleteCategory),
    path('categories/<int:id>/edit',stockController.editCategory),
    path('category/<int:id>/update',stockController.updateCategory),
]
