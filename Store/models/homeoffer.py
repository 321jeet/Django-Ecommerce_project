from django.db import models

class Offer(models.Model):
    des=models.CharField(max_length=200)
    photo =models.ImageField(upload_to='uploads/offer/')
    price=models.IntegerField( default=0,blank=True)
    sellprice =models.IntegerField(default=0,blank=True)



    @staticmethod
    def get_all_offer():
       return Offer.objects.all()