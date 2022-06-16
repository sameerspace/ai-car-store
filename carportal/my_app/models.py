from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=200)
    modelDate = models.CharField(max_length=4)
    mileage_km = models.PositiveIntegerField()
    displacement_cc = models.IntegerField()
    condition = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.manufacturer}  {self.modelDate}"


class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    location = models.CharField(max_length=100)


class VehicleImage(models.Model):
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
