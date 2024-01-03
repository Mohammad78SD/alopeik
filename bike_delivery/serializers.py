from .models import delivery_request
from rest_framework.serializers import ModelSerializer

class req_serializer(ModelSerializer):
    class Meta:
        model = delivery_request
        fields = '__all__'