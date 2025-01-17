from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.

def car_list(request):
    shop_app = Car.objects.all()
    return render(request, 'shop_app/shopApp.html', {'shop_app': shop_app})