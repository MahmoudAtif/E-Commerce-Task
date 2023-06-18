from rest_framework import serializers
from core.payment.models import Cart
from .cart_item_serilaizer import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    """Cart Serializer"""

    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(
        source='get_total_items',
        read_only=True
    )

    class Meta:
        model = Cart
        exclude = ['user']
