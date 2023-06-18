from rest_framework import viewsets, mixins
from core.products.models import Product
from core.products.serializers import ProductSerializer
from rest_framework.filters import SearchFilter


class ProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    """Product ViewSet"""

    queryset = (
        Product.objects.filter(status=True)
        .order_by('price')
    )
    serializer_class = ProductSerializer
    permission_classes = ()
    filter_backends = [SearchFilter]
    search_fields = ['name']
