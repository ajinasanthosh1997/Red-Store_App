
from django.contrib import admin
from django.urls import path

from . import views

app_name= 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>', views.product_details, name='products'),
    path('product_details/<int:pk>', views.product_details, name='product_details'),
    path('account/', views.account, name='account'),
    # path('cart/', views.cart, name='cart'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
