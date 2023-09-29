from django.urls import path
from . import views

app_name= 'cart'

urlpatterns = [
    # ... other URL patterns ...
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('place_order/', views.place_order, name='place_order'),
]