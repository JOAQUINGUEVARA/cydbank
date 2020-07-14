
# Register your models here.
from django.contrib import admin
from pedidos.models import Grupo,Especialidad,TipoInjerto,TipoIdentificacion,Eps,Pais,Departamento,Ciudad,PlanSalud,Tercero
from pedidos.models import EspecialidadInjerto,Solicitud,SolicitudDetalle,TipoCirugia,CiudadDireccion
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin

# Register your models here.

class TipoInjertoResource(resources.ModelResource):
    class Meta:
        model = TipoInjerto
        skip_unchanged = True
        report_skipped = True
        fields = ('idtipoinjerto','descripcion','especialidad','valor')        
        exclude = ('id',)

@ admin.register (TipoInjerto) 
class TipoInjertoAdmin (ImportExportModelAdmin):
    list_display= ('idtipoinjerto','descripcion','especialidad','caracteristicas','valor','activo','foto')
    list_select_related = ['especialidad']
    search_fields = ['descripcion']
    list_per_page = 50
    #autocomplete_fields = ['especialidad']
    #fields = ['idtipoinjerto', 'descripcion','especialidad','detalle','caracteristicas','valor','valor_descuento','activo','foto']

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = TipoIdentificacion
        skip_unchanged = True
        report_skipped = True
        fields = ('idtipoidentificacion','descripcion')        
        exclude = ('id',)

@ admin.register (TipoIdentificacion) 
class TipoIdentificacionAdmin (ImportExportModelAdmin):
    list_display= ('idtipoidentifica','descripcion')

class EpsResource(resources.ModelResource):
    class Meta:
        model = Eps
        skip_unchanged = True
        report_skipped = True
        fields = ('ideps','descripcion')        
        exclude = ('id',)

@ admin.register (Eps) 
class Eps(ImportExportModelAdmin):
    list_display= ('ideps','descripcion')
    search_fields = ['descripcion']
    list_per_page = 50

class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais
        skip_unchanged = True
        report_skipped = True
        fields = ('idpais','descripcion')        
        exclude = ('id',)

@ admin.register (Pais) 
class Pais(ImportExportModelAdmin):
    list_display= ('idpais','descripcion')
    search_fields = ['descripcion']
    list_per_page = 50


class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento
        skip_unchanged = True
        report_skipped = True
        fields = ('iddepartamento','pais','descripcion')        
        exclude = ('id',)

@ admin.register (Departamento)
class Departamento(ImportExportModelAdmin):
    list_display= ('iddepartamento','pais','descripcion')
    search_fields = ['descripcion']
    list_per_page = 50

class CiudadResource(resources.ModelResource):
    class Meta:
        model = Ciudad
        skip_unchanged = True
        report_skipped = True
        fields = ('idciudad','departamento','pais','descripcion')        
        exclude = ('id',)

@ admin.register (Ciudad)
class Ciudad(ImportExportModelAdmin):
    list_display= ('idciudad','departamento','pais','descripcion')
    search_fields = ['descripcion']
    list_per_page = 50
 
class PlanSaludResource(resources.ModelResource):
    class Meta:
        model = PlanSalud
        skip_unchanged = True
        report_skipped = True
        fields = ('idplan','descripcion')        
        exclude = ('id',)

@ admin.register (PlanSalud)
class PlanSalud(ImportExportModelAdmin):
    list_display= ('idplan','descripcion')
    search_fields = ['descripcion']
    list_per_page = 50

class TerceroResource(resources.ModelResource):
    class Meta:
        model = Tercero
        skip_unchanged = True
        report_skipped = True
        fields = ('identificacion','tipoidentificacion','nombre1','nombre2','apel1','apel2','razon_social','direccion','ciudad_direccion','telefono','email','eps','plan_salud','fecha_nacimiento','edad','pais','departamento','nacionalidad','ciudad','especialidad','tipo_ter','created','updated')        
        exclude = ('id',)

@ admin.register (Tercero)
class Tercero(ImportExportModelAdmin):
    list_display= ('id','identificacion','tipoidentificacion','nombre1','nombre2','apel1','apel2','razon_social','direccion','ciudad_direccion','telefono','email','eps','plan_salud','fecha_nacimiento','edad','pais','departamento','nacionalidad','ciudad','especialidad','tipo_ter','created','updated')
    search_fields = ['created']
    list_per_page = 50

class SolicitudResource(resources.ModelResource):
    class Meta:
        model = Solicitud
        skip_unchanged = True
        report_skipped = True
        fields = ('id','fecha','paciente','hospital','medico','pagador','tipo_cirugia','fecha_cirugia','valortotal','created','updated')        
        exclude = ('id',)

@ admin.register (Solicitud)
class Solicitud(ImportExportModelAdmin):
    list_display= ('id','fecha','paciente','hospital','medico','pagador','tipo_cirugia','fecha_cirugia','valortotal','created','updated')
    search_fields = ['fecha']
    list_per_page = 50

class SolicitudDetalleResource(resources.ModelResource):
    list_display= ('id','solicitud','tipoinjerto','cantidad','valor','valortotal','created','updated' )
    search_fields = ['created']
    list_per_page = 50

@ admin.register (SolicitudDetalle)
class SolicitudDetalle(ImportExportModelAdmin):
    list_display= ('id','solicitud','tipoinjerto','cantidad','valor','valortotal','created','updated' )
    search_fields = ['created']
    list_per_page = 50

class TipoCirugiaResource(resources.ModelResource):
    class Meta:
        model = TipoCirugia
        skip_unchanged = True
        report_skipped = True
        fields = ('idcirugia','descripcion')        
        exclude = ('id',)

@ admin.register (TipoCirugia)
class TipoCirugia(ImportExportModelAdmin):
    list_display= ('idcirugia','descripcion' )
    search_fields = ['idcirugia','descripcion']
    list_per_page = 50

class CiudadDireccionResource(resources.ModelResource):
    class Meta:
        model = CiudadDireccion
        skip_unchanged = True
        report_skipped = True
        fields = ('id','idciudad','descripcion')        
        exclude = ('id',)

@ admin.register (CiudadDireccion)
class CiudadDireccion(ImportExportModelAdmin):
    list_display= ('idciudad','descripcion' )
    search_fields = ['idciudad','descripcion']
    list_per_page = 50    

class EspecialidadResource(resources.ModelResource):
    class Meta:
        model = Especialidad
        skip_unchanged = True
        report_skipped = True
        fields = ('idespecial','descripcion')        
        exclude = ('id',)

@ admin.register (Especialidad)
class Especialidad(ImportExportModelAdmin):
    list_display= ('idespecial','descripcion' )
    search_fields = ['idespecial','descripcion']
    list_per_page = 50  
 
@ admin.register (EspecialidadInjerto)
class EspecialidadInjerto(admin.ModelAdmin):
    list_display= ('idespecial','descripcion' )
    search_fields = ['idespecial','descripcion']
    list_per_page = 50