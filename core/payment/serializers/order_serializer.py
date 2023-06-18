from rest_framework import serializers
from core.payment.models import Order
from .order_item_serializer import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer"""

    class Meta:
        model = Order
        exclude = ['user']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['status'] = Order.StatusEnum(instance.status).label
        return rep


class OrderDetailSerializer(serializers.ModelSerializer):
    """Order Detail Serializer"""

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        exclude = ['user']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['status'] = Order.StatusEnum(instance.status).label
        return rep
