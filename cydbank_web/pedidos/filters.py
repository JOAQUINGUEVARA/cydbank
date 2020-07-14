from pedidos.models import TipoInjerto,Tercero,Solicitud,SolicitudDetalle
import django_filters

class TipoInjertoFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='icontains')            
    class Meta:
        model = TipoInjerto
        fields = ['especialidad','descripcion']

class TerceroFilter(django_filters.FilterSet):
    class Meta:
        model = Tercero
        fields = ['created']

class SolicitudFilter(django_filters.FilterSet):
    #descripcion = django_filters.CharFilter(lookup_expr='icontains')            
    class Meta:
        model = Solicitud
        fields = ['created']        

class SolicitudDetalleFilter(django_filters.FilterSet):
    #descripcion = django_filters.CharFilter(lookup_expr='icontains')            
    class Meta:
        model = SolicitudDetalle
        fields = ['created']