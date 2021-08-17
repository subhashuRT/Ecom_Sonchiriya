from django.db import models
from all_category.models import Category

class Product(models.Model):
    items = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10,decimal_places=3)
    description = models.TextField() 
    image = models.ImageField(max_length=300,upload_to="product_images")
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.items
