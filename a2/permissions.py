from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsHRAuthenticated(BasePermission):
    """
    Allows access only to HR users (from custom HRLogin model)
    """
    def has_permission(self, request, view):
        auth = JWTAuthentication()
        try:
            validated_token = auth.get_validated_token(auth.get_raw_token(request.headers.get("Authorization").split(" ")[1]))
            # Extract email from token
            email = validated_token.get("email", None)
            if email:
                return True
        except Exception:
            raise AuthenticationFailed("Invalid or missing token")
        return False
