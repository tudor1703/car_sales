from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.core.paginator import Paginator

# Create your views here.

def car_list(request):
    shop_app = Car.objects.all()

    p = Paginator(Car.objects.all().order_by('order'), 2)
    page = request.GET.get('page')
    cars = p.get_page(page)

    return render(request, 'shop_app/shopApp.html', 
                  {'shop_app': shop_app,
                   'cars': cars})