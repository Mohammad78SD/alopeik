from django.urls import path
from .views import delivery_requests


urlpatterns = [
    path ("list", delivery_requests.as_view(), name = 'requests_list')
]