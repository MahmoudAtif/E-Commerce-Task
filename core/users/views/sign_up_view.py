from rest_framework import generics
from core.users.serializers import SignUpSerializer
from core.users.models import User


class SignUpView(generics.CreateAPIView):
    """SignUp View"""

    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = ()
