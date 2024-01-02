from django.contrib import admin
from .models import delivery_request

# Register your models here.
@admin.register(delivery_request)
class bike_delivery(admin.ModelAdmin):
    pass