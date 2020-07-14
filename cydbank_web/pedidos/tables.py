import django_tables2
from .models import TipoInjerto,SolicitudDetalleTemp,Solicitud,SolicitudDetalle
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

class InjertosTable(django_tables2.Table):
    valor = ColumnWithThousandsSeparator()
    pedido = django_tables2.TemplateColumn(
        '<a type="button" class="btn btn-primary" href="{% url "pedidos:ajax_add" record.id %}" value="pedir" >Pedir</a>',
        orderable=False
    )    
    class Meta:
        model = TipoInjerto
        #div_name = 'Stats_div'
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['descripcion','valor']
        attrs = {"class": "table table-hover table-sm"}

""" class ProductTable(tables.Table):
    tag_final_value = tables.Column(orderable=False, verbose_name='Price')
    action = tables.TemplateColumn(
        '<button class="btn btn-info add_button" data-href="{% url "ajax_add" instance.id record.id %}">Add!</a>',
        orderable=False
    )
    '<a type="button" class="btn btn-primary" href="{% url "pedidos:crea_detalle_pedido" record.id %}" value="pedir" >Pedir</a>',
 
    class Meta:
        model = Product
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'category', 'tag_final_value'] """



class DetallePedidoTable(django_tables2.Table):
    valor = ColumnWithThousandsSeparator()
    valortotal = ColumnWithThousandsSeparator()
    acción = django_tables2.TemplateColumn(
        '<form action="{% url "pedidos:borra_injerto" pk=record.id %}" method="POST">'
        '{% csrf_token %}'
        '<input class="btn btn-default btn-danger" type="submit" href="{% url "pedidos:borra_injerto" record.id %}" value="-"/>'
        '</form>'
        '<a type="button" class="btn btn-primary" href="{% url "pedidos:suma_injerto" record.id %}" value="+" >+</a>',
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
        fields = ['fecha','paciente','medico','hospital','pagador','ciudad_envio','direccion_envio','telefono_envio']
        attrs = {"class": "table table-hover table-sm"}

class SolicitudTable1(django_tables2.Table):
        
    class Meta:
        model = Solicitud
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['fecha','paciente','medico','hospital','pagador','valortotal']
        attrs = {"class": "table table-hover table-sm"}
        
class SolicitudesUnClienteTable(django_tables2.Table):
    valortotal = ColumnWithThousandsSeparator()
    Detalle = django_tables2.TemplateColumn(
        '<form action="{% url "pedidos:listar_un_pedido_de_un_cliente" record.id %}" method="POST">'
        '{% csrf_token %}'
        '<input class="btn btn-default btn-danger" type="submit" href="{% url "pedidos:listar_un_pedido_de_un_cliente" record.id %}" value="Ver Detalle"/>'
        '</form>',
     )
    
    class Meta:
        model = Solicitud
        #'medico','hospital','pagador',
        fields = ('fecha','paciente','medico','valortotal')
        #sequence = ('instance', 'name', )
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}

class SolicitudDetalleTable(django_tables2.Table):
        
    class Meta:
        model = SolicitudDetalle
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['tipoinjerto','cantidad','valor','valortotal']
        attrs = {"class": "table table-hover table-sm"}

class InjertosVitrinaTable(django_tables2.Table):
    valor = ColumnWithThousandsSeparator()
    pedido = django_tables2.TemplateColumn(
        '<a type="button" class="btn btn-primary" href="{% url "pedidos:crea_detalle_pedido" record.id %}" value="pedir" >Pedir</a>',
        orderable=False
    )        
