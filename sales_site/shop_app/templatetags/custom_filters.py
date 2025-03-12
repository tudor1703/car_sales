from django import template

register = template.Library()

@register.filter
def spaced_price(value):
    try:
        value = float(value)
        return f"{value:,.2f}".replace(",", " ") + "$"
    except (ValueError, TypeError):
        return value  # Return as is if not a valid number
