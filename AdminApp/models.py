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


class DesignCategoryDb(models.Model):
    CategoryName = models.CharField(max_length=100, unique=True)
    CategoryImage = models.ImageField(upload_to="Design Category", null=True, blank=True)

    def __str__(self):
        return self.CategoryName


class DesignsDb(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Designer = models.CharField(max_length=100, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Style = models.CharField(max_length=50, null=True, blank=True)
    Dimension = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="Interior Designs", null=True, blank=True)
    Estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.Name







