from import_export import resources
from .models import SolicitudDetalle
#from reservas.models import Meeting

class SolicitudResource(resources.ModelResource):
    class Meta:
        model = SolicitudDetalle