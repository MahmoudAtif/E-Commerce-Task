from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.utils.response_codes import response_codes
from rest_framework.permissions import IsAdminUser


class ResponseCodeView(APIView):
    """Response Code View"""
    permission_classes = [IsAdminUser]

    def get(self, request):
        codes = response_codes()
        return Response(data=codes, status=status.HTTP_200_OK)
