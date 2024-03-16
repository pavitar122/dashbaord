from django.contrib.auth.backends import BaseBackend
from .models import Doctor

class MyUserAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Doctor.objects.get(email=email)
            if user.check_password(password):
                return user
        except Doctor.DoesNotExist:
            return None