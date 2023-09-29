from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import Item
from .cart import CartManager
from django.http import JsonResponse
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

cart_manager = CartManager()

def cart_view(request):
    # Your implementation to display the cart goes here
    return render(request, 'cart/cart.html')  # Use your template path here

@login_required
def place_order(request):
    # Calculate the total order amount
    cart_tax = cart_manager.get_cart_tax(request)
    cart_total = sum(item.item.price * item.quantity for item in cart_manager.get_cart_items(request))
    cart_total_with_tax = cart_total + float(cart_tax)

    # Create an order
    order = Order.objects.create(user=request.user, total=cart_total_with_tax)

    # Create order items
    for cart_item in cart_manager.get_cart_items(request):
        OrderItem.objects.create(order=order, item=cart_item.item, quantity=cart_item.quantity)

    # Clear the cart or remove cart items here
    cart_manager.clear_cart(request)

    return render(request,'cart/order-confirmation.html')

def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        cart_manager.add_to_cart(request, item_id)
    else:
        cart = request.session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        request.session['cart'] = cart

    return redirect('cart:view_cart')


@login_required
def update_cart(request, cart_item_id):
    print('hello')
    if request.method == 'POST':
        print('hello')
        new_quantity = int(request.POST.get('new_quantity', 1))
        cart_manager.update_quantity(request, cart_item_id, new_quantity)
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    cart_manager = CartManager()
    cart_items = cart_manager.get_cart_items(request)
    cart_tax = cart_manager.get_cart_tax(request)  # Calculate cart tax here
    for cart_item in cart_items:
        cart_item.total_price = cart_item.item.price * cart_item.quantity
    cart_total = sum(item.item.price * item.quantity for item in cart_items)
    cart_total_with_tax = float(cart_total )+ float(cart_tax)  # Calculate total with tax here
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total, 'cart_tax': cart_tax, 'cart_total_with_tax': cart_total_with_tax})


def remove_from_cart(request, cart_item_id):
    cart_manager.remove_item(request, cart_item_id)
    return redirect('cart:view_cart')

