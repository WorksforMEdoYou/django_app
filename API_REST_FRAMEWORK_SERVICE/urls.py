from django.urls import path
from . import views

urlpatterns = [
    path('getproducts/', views.search_products, name='getproducts'),
    path('products/<int:pk>/update/', views.update_product, name='product-update'),
    path('products/<int:pk>/delete/', views.delete_product, name='product-delete'),
]