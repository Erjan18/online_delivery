from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserProfile(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user',]

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']