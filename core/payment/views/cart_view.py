from rest_framework.exceptions import NotFound
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.payment.models import Cart, Order, OrderItem
from core.utils.response_codes import GeneralCodes
from core.payment.serializers import (
    CartSerializer,
    AddToCartInputSerializer,
    UpdateItemQuantitySerializer,
    OrderInputSerilaizer,
    OrderDetailSerializer
)
from drf_spectacular.utils import extend_schema


class CartView(viewsets.GenericViewSet):
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def list(self, request, *args, **kwargs):
        """Cart ListView"""
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=AddToCartInputSerializer
    )
    @action(
        methods=['POST'],
        detail=False
    )
    def add(self, request, *args, **kwargs):
        """Add to cart"""
        serializer = AddToCartInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = self.get_object()

        # get product and quantity data from validated_data
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        # get item from cart
        item = cart.items.filter(product=product).first()
        # claculate total quantity
        item_quantity = getattr(item, 'quantity', 0)
        total_quantity = quantity + item_quantity

        # if the product exist in cart update quantity else create one
        if item:
            item.update_quantity(total_quantity)
        else:
            cart.add_item(
                product=product,
                quantity=total_quantity
            )
        return Response(
            {
                'code': GeneralCodes.SUCCESS
            },
            status=status.HTTP_200_OK
        )

    @action(
        methods={'POST'},
        detail=False,
        url_path=r'items/(?P<pk>[^/.]+)/remove'
    )
    def remove(self, *args, **kwargs):
        """Remove from cart"""
        cart = self.get_object()
        pk = self.kwargs.get('pk')

        item = cart.items.filter(id=pk).first()
        self._check_item(item)

        item.delete()
        return Response(
            {
                'code': GeneralCodes.SUCCESS
            },
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=UpdateItemQuantitySerializer
    )
    @action(
        methods={'POST'},
        detail=False,
        url_path=r'items/(?P<pk>[^/.]+)/update-quantity'
    )
    def update_quantity(self, request, *args, **kwargs):
        """Update item quantity"""
        serilaizer = UpdateItemQuantitySerializer(data=request.data)
        serilaizer.is_valid(raise_exception=True)

        cart = self.get_object()
        pk = self.kwargs.get('pk')
        quantity = serilaizer.validated_data['quantity']

        item = cart.items.filter(id=pk).first()
        self._check_item(item)

        # update quantity after check
        item.update_quantity(quantity)
        return Response(
            {
                'code': GeneralCodes.SUCCESS
            },
            status=status.HTTP_200_OK
        )

    @action(
        methods={'POST'},
        detail=False
    )
    def clear(self, *args, **kwargs):
        """Clear all products in the cart"""
        cart = self.get_object()
        cart.clear()
        return Response(
            {
                'code': GeneralCodes.SUCCESS
            },
            status=status.HTTP_200_OK
        )

    @extend_schema(
        request=OrderInputSerilaizer
    )
    @action(
        methods=['POST'],
        detail=False
    )
    def checkout(self, request, *args, **kwargs):
        """Create Order"""
        serializer = OrderInputSerilaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # get state and city data from validated_data
        state = serializer.validated_data['state']
        city = serializer.validated_data['city']
        # create order
        cart = self.get_object()
        order = Order.objects.create(
            user=request.user,
            total=cart.total,
            state=state,
            city=city
        )
        # add order items
        for item in cart.items.select_related('product'):
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        # clear all products from cart
        cart.clear()
        # return all data about the order
        order_detail_serializer = OrderDetailSerializer(order)
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
                'data': order_detail_serializer.data
            },
            status=status.HTTP_200_OK
        )

    def _check_item(self, item):
        """method to check the item"""
        if not item:
            raise NotFound(
                {
                    'code': GeneralCodes.NOT_FOUND
                }
            )
        return True
