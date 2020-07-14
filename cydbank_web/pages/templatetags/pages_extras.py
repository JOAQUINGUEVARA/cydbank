from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

@register.simple_tag
def faq_list():
    pages = Page.objects.all()
    return pages    