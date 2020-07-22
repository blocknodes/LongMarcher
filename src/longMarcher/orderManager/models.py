from django.db import models
from picklefield.fields import PickledObjectField
from django.conf import settings

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=12)
    customer = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    deliver_at = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

class MeetingRoom(models.Model):
    name = models.CharField(max_length=50)

class MeetingRoomBinding(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    meetin_room = models.ForeignKey("MeetingRoom", on_delete=models.CASCADE)
    date = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    # approved or not
    status = models.BooleanField(default=False)
    applyed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'applyer')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'approver')



