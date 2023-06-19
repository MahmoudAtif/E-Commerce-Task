from rest_framework import serializers
from core.utils.response_codes import UserCodes
from django.contrib.auth import authenticate


class SignInSerializer(serializers.Serializer):
    """SignIn Serializer"""

    username_or_email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        # authenticate user
        user = authenticate(username=username_or_email, password=password)
        if user is None:
            raise serializers.ValidationError(
                {
                    'code': UserCodes.INVALID_CREDENTIALS
                }
            )
        # add user instance to validated_data
        attrs['user'] = user
        return attrs
