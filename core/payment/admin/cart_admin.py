from django.contrib import admin
from core.payment.models import Cart
from .cart_item_admin import CartItemInline


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
