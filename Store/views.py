
from http.client import HTTPResponse
from django.views.generic import TemplateView
from django.views import View

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from.models.product import Product
from.models.categary import Categary
from.models.homeoffer import Offer
from.models.customer import Customer
from.models.orders import Order
from.models.productdetails import ProductDetail




# Create your views here.


class Shop(View):

    def post(self, request):
        produ= request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            qunatity = cart.get(produ)
            if qunatity:
                if remove:
                    if qunatity<=1:
                        cart.pop(produ)
                    else:    
                       cart[produ] = qunatity-1
                else:

                    cart[produ] = qunatity + 1
            else:
                cart[produ] = 1
        else:
            cart = {}
            cart[produ] = 1
        request.session['cart'] = cart
       
        return redirect('Store')

    def get(self, request):

        # cart= request.session.get('cart')
        # if not cart:
        #  request.session.cart['cart'] = { }

        alloffer = Offer.get_all_offer()
        Prd = None
        categaries = Categary.get_all_categary()

        CatId = request.GET.get('categary')
        if CatId:
            Prd = Product.objects.filter(categary=CatId)
        else:
            Prd = Product.get_all_products()

        data = {
            'products': Prd,
            'categary': categaries,
            'alloffers': alloffer
        }
        print('you are :', request.session.get('email'))
        return render(request, 'store.html', data)



class ProductView(View):
    def get(self,request,*args, **kwargs):
        slug=kwargs['slug']
        product=Product.objects.get(slug=slug)
        
        return render(request,'prodetail.html',{'products':product})


 ######################### second method to view fuctuon######################


# class ProductView(TemplateView):
#     template_name= 'prodetail.html'
#     def  get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         url_slug=kwargs['slug']
#         prodata= Product.objects.get(slug=url_slug)
#         context['product']=prodata
       
#         return context
    


class Cart(View):
    def get(self, request):
    
      ids =list(request.session.get('cart').keys())
      product= Product.get_all_products_by_id(ids)
      
      return render(request,'cart.html' ,{'products':product})





def CheckOut( request):
   if request.method =='POST':
      address=request.POST.get('address')
      phone=request.POST.get('phone')
      customer =request.session.get('customer')
      cart =request.session.get('cart')
      products=Product.get_all_products_by_id(list(cart.keys()))
    #   print(address,phone,customer,products)

      for producte in products:
        order=Order(product=producte,
                    customer=Customer(id=customer),
                    price=producte.price,
                    address=address,
                    phone=phone,
                   quantity=cart.get(str(producte.id))

                   )
        # print(order.placeOrder())  
        order.save()
        request.session['cart']={}

   
      return redirect('Cart')

class OrderView(View):
   
    def get(self,request):
     customer=request.session.get('customer')
     ordered =Order.get_order_by_customer(customer)
    
     return render(request,'order.html',{'orders':ordered})



def register(request):
    if request.method == 'POST':

        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        reat_password = request.POST.get('reat_psw')

        if password != reat_password:
            error = "password did not match"
            return render(request, 'singup.html', {'errors': error})
        else:
            customers = Customer(user_name=user_name, first_name=first_name,  last_name=last_name, phone=phone, email=email,
                                 password=password)
            customers.password = make_password(
                customers.password)            # password hashing
            customers.Register()
            return redirect('/')

    return render(request, 'singup.html')


def loginHandal(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('psw')
        customer = Customer.get_customer_by_email(email)
        error_massage = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('/')
            else:
                error_massage = "email and password did not match"
        else:
            error_massage = "password and password did not match"

        return render(request, 'login.html', {'errors': error_massage})


def LogOUT(request):

     request.session.clear()
     return redirect ('/')
