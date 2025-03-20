from django.db import models
from DesignApp.models import ConsultDb
from WebApp.models import OrderDb, PaymentDetails, OrderTracking

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


class DailyProgressDb(models.Model):
    WorkDetails = models.CharField(max_length=200, null=True, blank=True)
    WorkImage = models.ImageField(upload_to="Working progress", null=True, blank=True)
    consult = models.ForeignKey(ConsultDb, on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField(auto_now_add=True)


class TrackingDb(models.Model):
    order = models.ForeignKey(OrderDb, on_delete=models.CASCADE)
    payment = models.ForeignKey(OrderTracking, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)  # Optional tracking number
    carrier = models.CharField(max_length=100, null=True, blank=True)  # Carrier name (e.g., FedEx, UPS)
    status = models.CharField(max_length=100, default="In Transit")  # Current status of the shipment
    estimated_delivery_date = models.DateField(null=True, blank=True)  # Estimated delivery date
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the tracking was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the tracking was last updated

    def __str__(self):
        return f"Tracking for Order {self.order.id} - Carrier: {self.carrier}, Status: {self.status}"

