from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile, OTP

class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    role = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, phone_number=phone_number)
        user.groups.add(Group.objects.get(name=role))
        return user
    
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['phone_number', 'otp', 'time']