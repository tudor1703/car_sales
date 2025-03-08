from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.car_list, name="car_list"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
]
