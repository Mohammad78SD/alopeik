from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.username
    
class OTP(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    