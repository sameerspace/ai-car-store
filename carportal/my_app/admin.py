from django.contrib import admin

# Register your models here.
from .models import Vehicle, UserDetails, VehicleImage

admin.site.register(Vehicle)
admin.site.register(UserDetails)
admin.site.register(VehicleImage)
