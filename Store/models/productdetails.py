
from django.db import models
from .product import Product

class ProductDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='uploads/productDetails/')

    def __str__(self) :
        return  self.product.name