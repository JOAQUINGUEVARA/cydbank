import django_tables2
from .models import TipoInjerto,SolicitudDetalleTemp,Solicitud
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe
from django_tables2 import tables, TemplateColumn

from django.utils.html import format_html

class ImageColumn(django_tables2.Column):
    def render(self, value):
        return format_html(
            '<img src="{{ foto.url }}" height="50px", width="50px">',
            url=value
        )
class ColumnWithThousandsSeparator(django_tables2.Column):
    def render(self,value):
        return intcomma(value)

""" class InjertosTable(django_tables2.Table):
    valor = ColumnWithThousandsSeparator()
    pedido = django_tables2.TemplateColumn(
         '<button data-href="{% url "ajax_modify" record.id "add" %}" class="btn btn-success edit_button"><i class="fa fa-arrow-up"></i></button>',
        orderable=False
    ) """
    
    class Meta:
        model = TipoInjerto
        #div_name = 'Stats_div'
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['descripcion','valor']
        attrs = {"class": "table table-hover table-sm"}        


class DetallePedidoTable(django_tables2.Table):
    valor = ColumnWithThousandsSeparator()
    valortotal = ColumnWithThousandsSeparator()
    acción = django_tables2.TemplateColumn(
        '<form action="{% url "pedidos:borra_injerto" pk=record.id %}" method="POST">'
        '{% csrf_token %}'
        '<input onclick="return confirm("Are you sure you want to delete this?")" class="btn btn-default btn-danger" type="submit" href="{% url "pedidos:borra_injerto" record.id %}" value="Borrar"/>'
        '</form>',
        orderable=False
    )
    
    class Meta:
        model = SolicitudDetalleTemp
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['tipoinjerto','cantidad','valor','valortotal']
        #attrs = {'class': 'stats_table', 'div': 'body'}

class SolicitudTable(django_tables2.Table):
        
    class Meta:
        model = Solicitud
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['paciente','medico','hospital','pagador','ciudad_envio','direccion_envio','telefono_envio']
        attrs = {"class": "table table-hover table-sm"}


