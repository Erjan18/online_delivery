from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'store/hi.html')


def products_page(request):
    return render(request, 'store/products.html')


def costumer_page(request):
    return render(request, 'store/custumer.html')
