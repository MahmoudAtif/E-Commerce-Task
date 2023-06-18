from rest_framework import serializers
from core.products.models import Product


class AddToCartInputSerializer(serializers.Serializer):
    """Add To Cart Input Serializer"""

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(status=True)
    )
    quantity = serializers.IntegerField(default=1)
