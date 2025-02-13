from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserRegistrationDb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    conf_password = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)


class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
    Pro_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)



