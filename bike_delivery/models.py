from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class delivery_request(models.Model):
    user =  models.ForeignKey(User, on_delete=models.PROTECT, related_name='request_user')
    
    delivery_man = models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'request_delivery_man')
    
    description = models.CharField()
    
    # 1 = request, 2 = accepted by a delivery man, 3 = delivery, 4 = delivered
    status = models.IntegerField()
    
    origin_lat = models.IntegerField()
    origin_lon = models.IntegerField()
    
    dest_lat = models.IntegerField()
    dest_lon = models.IntegerField()
    
    price = models.IntegerField()
    