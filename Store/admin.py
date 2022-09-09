from django.contrib import admin

from .models import Order
from .models import Product
from .models import Categary
from .models import Offer
from .models import Customer

from .models import ProductDetail

#  diplay the name  all  in tabel


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','categary']

class AdminOffer(admin.ModelAdmin):
    list_display=['des']





class AdminCustomer(admin.ModelAdmin):
   list_display=['user_name','email']



class AdminOrder(admin.ModelAdmin):
   list_display=['address','phone']



# Register your models here.
admin .site.register(Product,AdminProduct)

admin .site.register(Categary)

admin .site.register(Offer,AdminOffer)


admin .site.register(Customer,AdminCustomer)

admin .site.register(Order,AdminOrder)

admin .site.register(ProductDetail)