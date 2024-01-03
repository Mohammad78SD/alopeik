from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, OTPSerializer
from .models import OTP,UserProfile
import jwt
import datetime
import random
from ippanel import Client, Error, HTTPError, ResponseCode

# Create your views here.
    
class UserLoginView(generics.CreateAPIView):
    serializer_class = OTPSerializer
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        role = request.data.get('role', 'Customer')  # default role is 'Customer'
        otp = random.randint(1000, 9999)
        OTP.objects.create(phone_number=phone_number, otp=otp)
        client = Client("8en9TUYaGHPVU-gCdUSCCe4XxHuZhZUp62SQTIkY7ho=")
        ptrn = {
            'code': otp
            }

        client.send_pattern('zz9qp2vzfbtairt', "+983000505", str(phone_number), ptrn)


        user, created = User.objects.get_or_create(username=phone_number)
        if created:
            UserProfile.objects.create(user=user, phone_number=phone_number)
            user.groups.add(Group.objects.get(name=role))

        return Response({'message': 'OTP sent'})
    
class VerifyOTPView(generics.GenericAPIView):
    serializer_class = OTPSerializer
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        otp_obj = OTP.objects.filter(phone_number=phone_number).order_by('-time').first()
        if otp_obj is None:
            return Response({'message': 'No OTP found for this phone number'}, status=400)
        
        if otp_obj.otp == int(otp):
            user = User.objects.filter(userprofile__phone_number=phone_number).first()
            if user is None:
                return Response({'message': 'No user found for this phone number'}, status=400)
            
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'alopeik', algorithm='HS256')
            return Response({'token': token})
        else:
            return Response({'message': 'OTP is not correct'})
        