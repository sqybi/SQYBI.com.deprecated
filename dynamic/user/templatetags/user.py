from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter()
def user_path(user_name):
    return user_name.replace('_', '-')
