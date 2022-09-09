from pickle import FALSE
from django.db import models


class Customer(models.Model):
    user_name=models.CharField(max_length=50,default='')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone =models.CharField(max_length=15)
    email   =models.EmailField( )
    password =models.CharField(max_length=200)
   


    def __str__(self):
        return self.first_name
 
    def Register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
          return Customer.objects.get(email=email)
        except:
            return False







