from django.urls import path
from dashboard import views
from dashboard.controllers import stockController
from dashboard.controllers import productController
from dashboard.controllers import outgoingController
from dashboard.controllers import expiredController
from dashboard.controllers import reportController
from dashboard.controllers import settingController
from dashboard.controllers import userController
from dashboard.controllers import searchController

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
    path('category/<int:id>/contents/', productController.allByCatId),
    
    # outgoing routes
    path('outgoing/',outgoingController.index),
    path('outgoing/<int:id>',outgoingController.destroy , name='outgoing.destroy'),
    
    # expired routes
    path('expired/',expiredController.index, name='expired.index'),
    path('expired/<int:id>',expiredController.destroy , name='expired.destroy'),
        
    # reports routes
    path('report/', reportController.index, name='report.index'),
    path('report/current', reportController.current, name='report.current'),
    path('report/outgoing', reportController.outgoing, name='report.outgoing'),
    path('report/expired', reportController.expired, name='report.expired'),
    
    # setting routes
    path('setting/', settingController.index, name='setting.index'),
    path('setting/updateuser/<int:id>', settingController.updateUser, name='setting.update'),
    path('setting/changeuserpassword/<int:id>', settingController.changePassword, name='setting.changePassword'),

    # users routes
    path('user/<int:id>/view',userController.index, name='user.index'),
    
    # search 
    
    path('search', searchController.search, name='search')
]