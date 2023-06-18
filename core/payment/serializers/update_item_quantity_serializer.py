from rest_framework import serializers


class UpdateItemQuantitySerializer(serializers.Serializer):
    """Update Item Quantity Serializer"""

    quantity = serializers.IntegerField()
