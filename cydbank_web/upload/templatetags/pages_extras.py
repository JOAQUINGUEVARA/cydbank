from django import template
from upload.models import Document

register = template.Library()

@register.simple_tag
def get_abeas_list():
    document =  Document.objects.filter(id=1)
    return document

@register.simple_tag
def get_privacidad_list():
    document =  Document.objects.filter(id=2)
    return document    

@register.simple_tag
def get_acta_junta_list():
    document =  Document.objects.filter(id=3)
    return document    

@register.simple_tag
def get_certificacion_estados_financieros_list():
    document =  Document.objects.filter(id=4)
    return document

@register.simple_tag
def get_certificacion_cargos_list():
    document =  Document.objects.filter(id=5)
    return document

@register.simple_tag
def get_certificacion_antecedentes_list():
    document =  Document.objects.filter(id=6)
    return document

@register.simple_tag
def get_informe_revisor_list():
    document =  Document.objects.filter(id=7)
    return document

@register.simple_tag
def get_estados_financieros_list():
    document =  Document.objects.filter(id=8)
    return document

@register.simple_tag
def get_informe_junta_list():
    document =  Document.objects.filter(id=9)
    return document

@register.simple_tag
def get_declaracion_renta_list():
    document =  Document.objects.filter(id=10)
    return document
