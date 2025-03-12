from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Car
from .forms import OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

VALID_SORT_FIELDS = {"make", "model", "year"}


def car_list(request):
    order_by = request.GET.get("order_by", "make")

    if order_by not in VALID_SORT_FIELDS:
        order_by = "make"

    cars = Car.objects.all().order_by(order_by)

    paginator = Paginator(cars, 2)
    page_number = request.GET.get("page")
    cars_page = paginator.get_page(page_number)

    form = OrderForm(initial={"order_by": order_by})

    return render(
        request,
        "shop_app/shopApp.html",
        {
            "cars": cars_page,
            "form": form,
            "order_by": order_by,
        },
    )


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Use .get() to prevent errors
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "You have to fill in the spaces.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect(request.GET.get("next", "car_list"))  
            # Redirect back or to 'car_list'
        else:
            messages.error(request, "Invalid username or password. Try again!")
            return redirect("login")

    return render(request, "shop_app/login.html")

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered Succesfully!")
            return redirect('car_list')
        else:
            messages.success(request, "Whooops something went wrong! Try again")
            return redirect('register')

    return render(request, 'shop_app/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect(request.META.get('HTTP_REFERER', 'car_list'))
