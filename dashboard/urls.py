from django.urls import path
from dashboard import views
from dashboard.controllers import stockController
from dashboard.controllers import productController
from dashboard.controllers import outgoingController

urlpatterns = [
    path('', views.home),
    path('stock/', stockController.index),
    path('stock/create/', stockController.createProduct),
    path('categories/', stockController.categoriesIndex),
    path('category/create/', stockController.createCategory),
    path('categories/<int:id>/delete', stockController.deleleteCategory),
    path('categories/<int:id>/edit', stockController.editCategory),
    path('category/<int:id>/update', stockController.updateCategory),
    path('category/chechexpire/',stockController.checkExpirableCategory, name='checkexpire'),

    # products routes
    path('product/', productController.index, name='product.index'),
    path('product/create', productController.create, name='product.create'),
    path('product/store', productController.store, name='product.store'),
    path('product/<int:id>/show', productController.show, name='product.show'),
    path('product/<int:id>/edit', productController.edit, name='product.edit'),
    path('product/<int:id>/update', productController.update, name='product.update'),
    path('product/<int:id>/destroy', productController.destroy, name='product.destroy'),
    path('product/<int:id>/export', productController.export, name='product.export'),
    
    #outgoing routes
    path('outgoing/',outgoingController.index)
    
    
]
