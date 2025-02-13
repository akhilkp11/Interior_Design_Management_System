from django.db import models


# Create your models here.

class CategoryDb(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    # Description = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.ImageField(upload_to="Category Images", null=True, blank=True)


class ProductDb(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    category_name = models.CharField(max_length=100, null=True, blank=True)
    sub_category_name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to="Product Images", null=True, blank=True)










