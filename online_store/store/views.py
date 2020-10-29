from django.shortcuts import render,redirect
from .models import *
from .forms import Orderform
from .filters import OrderFilterSet
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'store/register.html',context)


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

def costumer_page(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    filterset = OrderFilterSet(request.GET,queryset=orders)
    orders = filterset.qs #Обращение к model
    context = {'customer':customer,'orders':orders,'orders_count':orders_count,'filterset':filterset}
    return render(request,'store/customer.html',context)

def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
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
