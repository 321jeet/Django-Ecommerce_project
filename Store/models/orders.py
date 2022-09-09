from datetime import datetime
from django.db import models
from . import Product
from . import Customer
import datetime

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE )
    
    quantity=models.IntegerField(default=1)
    price =models.IntegerField(default=0)
    address =models.CharField(max_length=200, default=" ")
    phone = models.CharField(max_length=10)
    date =models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    

     

    def placeOrder (self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
       return Order.objects.filter(customer=customer_id)