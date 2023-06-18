from rest_framework import serializers
from core.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product Serilaizer"""

    class Meta:
        model = Product
        fields = '__all__'
