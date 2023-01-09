from django.db import models
from service_sector.flat.models import Flat

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)