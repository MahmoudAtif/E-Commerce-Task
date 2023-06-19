from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.users.serializers import SignInSerializer
from core.utils.response_codes import GeneralCodes
from rest_framework_simplejwt.tokens import RefreshToken


class SignInView(APIView):
    """SignIn View"""

    serializer_class = SignInSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get user from validated_data
        user = serializer.validated_data['user']
        # generate access token and refresh token for authenticated user
        token = RefreshToken.for_user(user)
        return Response(
            {
                'code': GeneralCodes.SUCCESS,
                'refresh_token': str(token),
                'access_token': str(token.access_token),
            },
            status=status.HTTP_200_OK
        )
