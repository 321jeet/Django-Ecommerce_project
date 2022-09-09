
from django.urls import path
from Store import views
from .views import Shop ,Cart ,OrderView,ProductView
# from  Store.middleware.auth import auth_middlewares


urlpatterns = [
   
    path('', Shop.as_view(), name='Store'),
    path('singup', views.register, name='register'),
    path('login/', views.loginHandal, name='login'),
    path('logout', views.LogOUT, name='logout'),
    path("cart/", Cart.as_view(), name='Cart'),
    path("check-out", views.CheckOut, name='CheckOut'),
    path("order",OrderView.as_view(), name='Order'),
    path("prodetail/<slug:slug>/",ProductView.as_view(), name='Prodetail'),

]
