from django_filters import FilterSet
from .models import *
from django .forms import DateField
class OrderFilterSet(FilterSet):
    # start_date = DateField
    # end_date = DateField
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']