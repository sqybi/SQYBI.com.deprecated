from django import template

register = template.Library()

@register.filter
def abstract(value, arg = 100):
    """Generate abstract by given HTML document (value) and length (arg)"""
    return value[:arg]

