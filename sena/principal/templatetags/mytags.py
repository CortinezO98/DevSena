from django import template
import base64

register = template.Library()

@register.filter
def base64encode(url):
    url_encoded = base64.b64encode(url.encode()).decode()
    return url_encoded.replace('/', '_')