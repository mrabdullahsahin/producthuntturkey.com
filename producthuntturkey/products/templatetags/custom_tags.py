from django import template

register = template.Library()

@register.simple_tag
def language_url(value, arg):
    if arg == "en":
        return value.split('/')[2]
    elif arg == "tr":
        return value.split('/')[2]

register.filter('language_url', language_url)