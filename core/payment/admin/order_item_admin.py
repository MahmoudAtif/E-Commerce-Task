from django.contrib import admin
from core.payment.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1
