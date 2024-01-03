from django.shortcuts import render
from .models import delivery_request
from .serializers import req_serializer
from rest_framework import generics

class delivery_requests (generics.ListAPIView):
    queryset = delivery_request.objects.all()
    serializer_class = req_serializer
