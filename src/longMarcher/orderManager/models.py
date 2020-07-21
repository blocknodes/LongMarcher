from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=12)
    customer = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    deliver_at = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_paid = models.DecimalField(max_digits=10, decimal_places=2)
    extra_info = PickledObjectField()
