from rest_framework import serializers
from core.payment.models import CartItem
from core.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    """Cart Item Serializer"""

    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        exclude = ['cart']
