from django.db import models


class Car(models.Model):
    TRANSMISION_TYPE_CHOICE = [
        ("mecanica", "Mecanica"),
        ("automata", "Automata"),
    ]
    CONSUME_TYPE = [
        ("diesel", "Diesel"),
        ("plugin_hybrid", "Plug-in Hybrid"),
        ("hybrid", "Hybrid"),
        ("benzine", "Benzine"),
        ("electric", "Electric"),
    ]
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveBigIntegerField()
    mileage = models.PositiveBigIntegerField(default=0)
    fuel_type = models.CharField(max_length=16, choices=CONSUME_TYPE, default="diesel")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.CharField(
        max_length=10, choices=TRANSMISION_TYPE_CHOICE, default="mecanica"
    )
    image = models.ImageField(upload_to="car_images/", null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
