from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
   path('',home_page),
   path('products/',products_page),
   path('custumer/',costumer_page),
]