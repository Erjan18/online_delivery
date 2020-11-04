from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
   path('',home_page,name='home'),
   path('register/',register,name='register'),
   path('user/', user_page,name= 'user'),
   path('login/',login_page,name='login'),
   path('settings/',account_settings, name ='settings'),
   path('logout/',logout_page,name='logout'),
   path('products/',products_page,name='products'),
   path('customer/<int:pk>/',costumer_page,name='customer_page'),
   path('create_order/<int:pk>/',create_order,name='create_order'),
   path('update_order/<int:pk>/',update_order,name='update_order'),
   path('delete_order/<int:pk>/',delete_order,name='delete_order'),
]
