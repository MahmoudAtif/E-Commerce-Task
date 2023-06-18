from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from core.payment.models import Order
from core.utils.response_codes import GeneralCodes
from core.payment.serializers import OrderSerializer, OrderDetailSerializer


class OrderViewset(viewsets.GenericViewSet):
    """Order Viewset"""

    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk, *args, **kwargs):
        order = Order.objects.filter(id=pk, user=request.user).first()
        self._check_order(order)
        serializer = OrderDetailSerializer(order)
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @action(
        methods=['POST'],
        detail=True,
    )
    def cancel(self, request, pk, *args, **kwargs):
        """Cancel Order"""
        order = Order.objects.filter(id=pk, user=request.user).first()
        self._check_order(order)
        # change order status
        order.status = Order.StatusEnum.CANCELED
        order.save()
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
            },
            status=status.HTTP_200_OK
        )

    def _check_order(self, order):
        """method to check the order"""
        if not order:
            raise NotFound(
                {
                    'code': GeneralCodes.NOT_FOUND
                }
            )
        return True
