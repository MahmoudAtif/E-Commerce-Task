from rest_framework import serializers
from core.users.models import User
from core.utils.response_codes import UserCodes, GeneralCodes


class SignUpSerializer(serializers.ModelSerializer):
    """SignUp  Serializer"""

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        # to hash the password
        user = self.Meta.model.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')

        # check password and confirm_password
        if password != confirm_password:
            raise serializers.ValidationError(
                {
                    'code': UserCodes.PASSWORD_NOT_MATCH
                }
            )

        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['code'] = GeneralCodes.SUCCESS
        return rep
