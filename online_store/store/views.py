from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import Orderform, UserProfile
from .filters import OrderFilterSet
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .decorators import *

@unauth_user
def register(request):
    form = CustomerRegisterForm()
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success registration')
            return redirect('home')
    context = {'form':form}
    return render(request, 'store/register.html',context)

def user_page(request):
    orders = request.user.customer.order_set.all()
    context = {'orders':orders}
    return render(request, 'store/user.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        # if user is not None:
        return redirect('home')
    context = {}
    return render(request,'store/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home_page(request):
    orders_count = Order.objects.all().count()
    orders = Order.objects.all()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    customers = Customer.objects.all()
    context = {'customers': customers,'orders_count':orders_count,'delivered':delivered,'orders':orders,'pending':pending}
    return render(request, 'store/hi.html',context)

def products_page(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'store/products.html',context)
@admin_only
def costumer_page(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    filterset = OrderFilterSet(request.GET,queryset=orders)
    orders = filterset.qs #Обращение к model
    context = {'customer':customer,'orders':orders,'orders_count':orders_count,'filterset':filterset}
    return render(request,'store/customer.html',context)

def account_settings(request):
    user =request.user.customer
    form = UserProfile(instance=user)
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'store/account.html', context)

def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,'customer':customer}
    return render(request,'store/order_form.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'store/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request,'store/delete.html',context)
