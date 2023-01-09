from django.db import models
from service_sector.house.models import House


# Create your models here.
class Flat(models.Model):
    date_modified = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(to=House, on_delete=models.CASCADE)
    number = models.IntegerField()
    floor = models.IntegerField()
    way_desc = models.CharField(max_length=500)
