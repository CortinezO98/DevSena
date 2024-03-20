from django import template
import base64

register = template.Library()

@register.filter
def base64encode(value):
    encoded_bytes = base64.b64encode(value.encode())
    return encoded_bytes.decode()