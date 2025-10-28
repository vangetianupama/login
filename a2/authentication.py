from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import AccessToken
from .models import HRLogin

class HRJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                return None

            decoded = AccessToken(token)
            email = decoded.get("email")

            if not email:
                raise exceptions.AuthenticationFailed("Invalid token")

            hr = HRLogin.objects.filter(email=email).first()
            if not hr:
                raise exceptions.AuthenticationFailed("User not found")

            #  Add .is_authenticated dynamically
            hr.is_authenticated = True
            return (hr, None)

        except Exception:
            raise exceptions.AuthenticationFailed("Invalid or expired token")