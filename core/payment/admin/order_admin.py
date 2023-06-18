from django.contrib import admin
from core.payment.models import Order
from .order_item_admin import OrderItemInline


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
