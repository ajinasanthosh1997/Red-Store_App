from .models import Cart, CartItem, Order, OrderItem
from django.conf import settings
from mainapp.models import Item
from decimal import Decimal
from django.contrib.auth.decorators import login_required

CART_SESSION_KEY = getattr(settings, 'CART_SESSION_KEY', 'cart_id')

class CartManager:
    def get_cart(self, request):
        if request.user.is_authenticated:
            # If the user is logged in, get the most recent cart associated with the user
            cart = Cart.objects.filter(user=request.user).order_by('-created_at').first()
            if not cart:
                cart = Cart.objects.create(user=request.user)
        else:
            # If the user is not logged in, use session-based cart
            cart_id = request.session.get(CART_SESSION_KEY)
            if cart_id:
                cart = Cart.objects.get(pk=cart_id)
            else:
                cart = Cart.objects.create(user=None)  # Create a non-authenticated cart
                request.session[CART_SESSION_KEY] = cart.id
        return cart
    
    def add_to_cart(self, request, item_id):
        cart = self.get_cart(request)
        item = Item.objects.get(pk=item_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        cart_item.quantity += 1
        cart_item.save()
    
    def get_cart_items(self, request):
        cart = self.get_cart(request)
        return cart.cartitem_set.all()

    def update_quantity(self, request, cart_item_id, new_quantity):
        cart = self.get_cart(request)
        cart_item = CartItem.objects.get(pk=cart_item_id)
        if cart_item.cart == cart:
            cart_item.quantity = new_quantity
            cart_item.save()

    def remove_item(self, request, cart_item_id):
        cart = self.get_cart(request)
        cart_item = CartItem.objects.get(pk=cart_item_id)
        if cart_item.cart == cart:
            cart_item.delete()

    def get_cart_tax(self, request):
        cart_items = self.get_cart_items(request)
        tax_rate = Decimal('0.10')
        cart_tax = sum(Decimal(item.item.price) * item.quantity * tax_rate for item in cart_items)
        return cart_tax    
    
    def create_order(self, request, cart_total_with_tax):
        cart = self.get_cart(request)
        order = Order.objects.create(user=request.user, total=cart_total_with_tax)

        for cart_item in cart.cartitem_set.all():
            OrderItem.objects.create(order=order, item=cart_item.item, quantity=cart_item.quantity)

        # Clear the cart or remove cart items here
        cart.cartitem_set.all().delete()
        return order

    # @login_required
    def clear_cart(self, request):
        # Clear the user's cart if logged in
        if request.user.is_authenticated:
            cart = self.get_cart(request)
            if cart.user == request.user:
                cart.cartitem_set.all().delete()
        else:
            # Handle clearing of session-based cart for non-authenticated users
            cart_id = request.session.get(CART_SESSION_KEY)
            if cart_id:
                Cart.objects.filter(pk=cart_id).delete()
                del request.session[CART_SESSION_KEY]
