from django import template


register = template.Library()

@register.filter(name='split_length')
def split_length(value):
    return len(value.split(','))