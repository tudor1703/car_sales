from django import forms

CHOICES = [
    ('make', 'Make'),
    ('model', 'Model'),
    ('year', 'Year'),
]

class OrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=True,
        label="Sort by",
    )
