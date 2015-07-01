from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='myfilter')
@stringfilter
def myfilter(value, arg):
    return value.upper()+arg


@register.filter(needs_autoescape=True)
def initial_letter_filter(value, autoescape=None):
    first, other = value[0], value[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)


@register.filter(needs_autoescape=False)
@register.filter(name='add_code')
def add_code(value):
    # if autoescape:
    #     esc = conditional_escape
    # else:
    #     esc = lambda x: x
    # result = esc(value)
    return mark_safe(value)