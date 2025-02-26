from django.db import models

# Create your models here.


class ConsultDb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    design_id = models.IntegerField(unique=True)
    design_category = models.CharField(max_length=100)
    design_name = models.CharField(max_length=100)
    design_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    design_dimension = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
