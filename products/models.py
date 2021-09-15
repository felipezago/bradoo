from django.db import models
from vendors.models import Vendors


class Products(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=14)
    price = models.FloatField()
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='products')
