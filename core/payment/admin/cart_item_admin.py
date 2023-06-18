from django.contrib import admin
from core.payment.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']


class CartItemInline(admin.StackedInline):
    model = CartItem
    extra = 1
