from django.contrib import admin
from . models import Cart,CartItem,Order,OrderItem
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of OrderItem forms to display inline

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)