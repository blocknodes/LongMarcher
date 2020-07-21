from django.db import models
from picklefield.fields import PickledOjbectField

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=12)
    customer = models.CharField()
    create_at = models.DateField(auto_now_add=True)
    deliver_at = models.DateField()
    price = models.DecimalField(decimal_places=2)
    pre_paid = models.DecimalField(decimal_places=2)
    extra_info = PickledOjbectField()
