from django.db import models

# Create your models here.

#модель = таблица

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, primary_key=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name