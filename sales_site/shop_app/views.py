from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Car
from .forms import OrderForm

VALID_SORT_FIELDS = {'make', 'model', 'year'}

def car_list(request):
    order_by = request.GET.get('order_by', 'make')

    if order_by not in VALID_SORT_FIELDS:
        order_by = 'make'

    cars = Car.objects.all().order_by(order_by)

    paginator = Paginator(cars, 2) 
    page_number = request.GET.get('page') 
    cars_page = paginator.get_page(page_number)

    form = OrderForm(initial={'order_by': order_by}) 

    return render(request, 'shop_app/shopApp.html', {
        'cars': cars_page,
        'form': form,
        'order_by': order_by,  
    })
