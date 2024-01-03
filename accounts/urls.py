from django.urls import path
from .views import UserLoginView, VerifyOTPView

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('verify-otp', VerifyOTPView.as_view(), name='verify-otp'),
]