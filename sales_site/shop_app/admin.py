from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'mileage', 'fuel_type', 'price', 'description', 'type', 'image')  # Columns in admin listing
    search_fields = ('make', 'model', 'year')  # Search fields