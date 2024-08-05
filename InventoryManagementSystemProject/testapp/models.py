from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=200)
    sku = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity_in_stack = models.IntegerField()
    