

from uuid import uuid4
import uuid
from  django.db import models
from .categary import Categary

class Product(models.Model):
    
    name=models.CharField(max_length=50)
    title =models.CharField(max_length=200 ,default=' ')
    slug=models.SlugField(unique=True ,default=0)
    price =models.IntegerField(default=0)
    sellprice =models.IntegerField()
    categary =models.ForeignKey(Categary,on_delete=models.CASCADE , default=1)
    descriptions =models.CharField(max_length=200,default='',null=True ,blank=True)
    image =models.ImageField(upload_to='uploads/products/')
    time=models.TimeField(auto_now=True)


    def __str__(self) :
        return self.name
      

    @staticmethod
    def get_all_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


  


  




  