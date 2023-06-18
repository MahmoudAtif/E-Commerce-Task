from rest_framework import serializers
from core.payment.models import OrderItem
from core.products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """Order Item Serializer"""

    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        exclude = ['order']
