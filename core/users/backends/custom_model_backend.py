from django.contrib.auth.backends import ModelBackend
from core.users.models import User
from django.db.models import Q

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs) :
        user = User.objects.filter(
           Q(username=username) |
           Q(email=username)
        ).first()

        if user is None or not user.check_password(password):
            return None
        
        return user