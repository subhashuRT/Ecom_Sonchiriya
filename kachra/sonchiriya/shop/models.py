from django.db import models
from django.db import models

# Create your models here.
class Products(models.Model):
    items = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    discounted_price = models.DecimalField(max_digits=10,decimal_places=3)
    category = models.CharField(max_length=120)
    description = models.TextField() 
    image = models.CharField(max_length=300)