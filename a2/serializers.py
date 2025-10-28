from rest_framework import serializers
from .models import Job, HRLogin
from rest_framework_simplejwt.tokens import RefreshToken

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class HRLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRLogin
        fields = ['email', 'password']


class MyTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            hr = HRLogin.objects.get(email=email, password=password)
        except HRLogin.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Manually create tokens
        refresh = RefreshToken()
        access = refresh.access_token

        # Custom claims (so we can recognize HR)
        refresh["hr_id"] = hr.id
        refresh["email"] = hr.email
        access["hr_id"] = hr.id
        access["email"] = hr.email

        return {
            "refresh": str(refresh),
            "access": str(access)
        }
