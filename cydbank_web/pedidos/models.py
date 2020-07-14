from django.db import models
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.timezone import now
from .managers import InjertoManager
from django.db.models import Sum

# Create your models here.

CURRENCY = settings.CURRENCY


class Grupo(models.Model):
	idgrupo=models.CharField(max_length=2,blank=True,default='',verbose_name='Código Grupo')
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Grupo'
		verbose_name_plural='Grupos'

	def __str__(self):
		return self.descripcion

class Especialidad(models.Model):
	idespecial=models.CharField(max_length=3,blank=True,default='',verbose_name='Código Especialidad')
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Especialidad'
		verbose_name_plural='Especialidades'

	def __str__(self):
		return self.descripcion

class TipoInjertoManager(models.Manager):

    def active(self):
        return self.filter(activo=True)

class EspecialidadInjerto(models.Model):
	idespecial=models.CharField(max_length=2,blank=True,default='',verbose_name='Código Especialidad')
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Especialidad Injerto'
		verbose_name_plural='Especialidades Injertos'

	def __str__(self):
		return self.descripcion

class InjertosActivosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)

class TipoInjerto(models.Model):
	idtipoinjerto=models.CharField(max_length=4,blank=True,default='',verbose_name='Código Tipo de Injerto')
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')
	especialidad=models.ForeignKey(EspecialidadInjerto,on_delete=models.CASCADE,verbose_name='Especialidad Injerto')
	#grupo=models.ForeignKey(Grupo,on_delete=models.CASCADE,verbose_name='Grupo')
	valor=models.DecimalField(max_digits=10, decimal_places=2, default=0.00,verbose_name='Precio')
	#valor_descuento=models.DecimalField(max_digits=10, decimal_places=2, default=0.00,verbose_name='Descuento')
	#valor_final=models.DecimalField(max_digits=10, decimal_places=2, default=0.00,verbose_name='Precio')
	caracteristicas=models.CharField(max_length=2000,blank=True,default='',verbose_name='Características')
	activo = models.BooleanField(default=True)
	foto = models.ImageField(verbose_name="Foto", upload_to="fotos_injertos",null=True,blank=True,default='static/img/placeholder.jpg')

	injertos_activos = InjertosActivosManager()

	class Meta:
		ordering=["idtipoinjerto"]
		verbose_name='Tipo de Injerto'
		verbose_name_plural='Tipos de Injertos'

	def __str__(self):
		return self.descripcion
		#cadena="{0},{0}"
		#return cadena.format(self.Especialidad.descripcion,self.Grupo.descripcion) 

	def get_foto(self):
		if self.foto and hasattr(self.foto, 'url'):
			return self.foto.url
		else:
			return '/fotos_injertos/'

class TipoIdentificacion(models.Model):
	idtipoidentifica=models.CharField(max_length=2,null=True,blank=True,default='',verbose_name='Código')
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo de Identificacion'
		verbose_name_plural='Tipos de Identificacion'

	def __str__(self):
		return self.descripcion

class Eps(models.Model):
	ideps=models.CharField(max_length=3,null=True,blank=True,default='',verbose_name='Código')
	descripcion=models.CharField(max_length=300,verbose_name='Descripción')
	#created=models.DateField(auto_now_add=True,verbose_name='Fecha de Creación')
	#updated=models.DateField(auto_now_add=True,verbose_name='Fecha de Edición')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Eps'
		verbose_name_plural='Eps'

	def __str__(self):
		return self.descripcion

class Pais(models.Model):
	idpais=models.CharField(max_length=3,null=True,blank=True,default='',verbose_name='Código País')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='País'
		verbose_name_plural='Países'

	def __str__(self):
		return self.descripcion

class Departamento(models.Model):
	iddepartamento=models.CharField(max_length=3,null=True,blank=True,default='',verbose_name='Código Departamento')
	pais=models.ForeignKey(Pais,null=False,blank=False,on_delete=models.CASCADE,default='0',verbose_name='País')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Departamento'
		verbose_name_plural='Departementos'

	def __str__(self):
		return self.descripcion

class Ciudad(models.Model):
	idciudad=models.CharField(max_length=5,null=True,blank=True,default='',verbose_name='Código Ciudad')
	departamento=models.ForeignKey(Departamento,blank=False,on_delete=models.CASCADE,default='0',verbose_name='Departamento')
	pais=models.ForeignKey(Pais,null=False,blank=False,on_delete=models.CASCADE,default='0',verbose_name='País')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Ciudad'
		verbose_name_plural='Ciudades'

	def __str__(self):
		#return self.descripcion
		return str(self.descripcion).strip()+"-"+str(self.departamento).strip()

class PlanSalud(models.Model):
	idplan=models.CharField(max_length=2,blank=True,default='',verbose_name='Código Plan')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Plan Salud'
		verbose_name_plural='Planes Salud'

	def __str__(self):
		return self.descripcion

class TipoCirugia(models.Model):
	idcirugia=models.CharField(max_length=4,blank=True,default='',verbose_name='Código Cirugía')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Cirugía'
		verbose_name_plural='Tipo Cirugía'

	def __str__(self):
		return self.descripcion

class CiudadDireccion(models.Model):
	idciudad=models.CharField(max_length=5,blank=True,default='',verbose_name='Código Ciudad')
	descripcion=models.CharField(max_length=35,verbose_name='Descripción')
	departamento=models.ForeignKey(Departamento,blank=False,on_delete=models.CASCADE,default='0',verbose_name='Departamento')
	pais=models.ForeignKey(Pais,null=False,blank=False,on_delete=models.CASCADE,default='0',verbose_name='País')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Ciudad Direección'
		verbose_name_plural='Ciudades Dirección'

	def __str__(self):
		#return self.descripcion
		return str(self.descripcion).strip()+"-"+str(self.departamento).strip()

class Tercero(models.Model):
	TIPO_TER = (
        ('Paciente','Paciente'),
		('Hospital','Hospital'),
        ('Medico','Medico'),
        ('Pagador','Pagador'),
    )
	identificacion=models.CharField(max_length=15,null=True,blank=True,default='',verbose_name='Nro. Identificación')
	tipoidentificacion=models.ForeignKey(TipoIdentificacion,max_length=2,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Tipo de Indetificación')
	nombre1 = models.CharField(max_length=25,blank=True,default='',verbose_name='Primer Nombre')
	nombre2 = models.CharField(max_length=25,blank=True,default='',verbose_name='Segundo Nombre')
	apel1 = models.CharField(max_length=25,blank=True,default='',verbose_name='Primer Apellido')
	apel2 = models.CharField(max_length=25,blank=True,default='',verbose_name='Segundo Apellido')
	razon_social = models.CharField(max_length=50,null=True,blank=True,default='',verbose_name='Razon Social')
	direccion = models.CharField(max_length=100,blank=True,default='',verbose_name='Dirección')
	ciudad_direccion = models.ForeignKey(CiudadDireccion,max_length=5,null=True,blank=True,default='1112',on_delete=models.CASCADE,verbose_name='Ciudad Direcciòn')
	telefono = models.CharField(max_length=35,blank=True,default='',verbose_name='Teléfono')
	email = models.CharField(max_length=50,blank=True,default='',verbose_name='Email')
	eps = models.ForeignKey(Eps,max_length=3,null=True,blank=True,default=1,on_delete=models.CASCADE,verbose_name='EPS')
	plan_salud = models.ForeignKey(PlanSalud,null=True,blank=True,default=1,on_delete=models.CASCADE,verbose_name='Plan Salud')
	fecha_nacimiento = models.DateField(null=True,blank=True,default='1900-01-01',verbose_name='Fecha de Nacimiento DD/MM/AAAA')
	edad = models.PositiveIntegerField(null=True,blank=True,default=0,verbose_name='Edad')
	pais = models.ForeignKey(Pais,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='País Nacimiento')
	departamento = models.ForeignKey(Departamento,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Departamento Nacimiento')
	nacionalidad = models.CharField(blank=True,default='',max_length=80,verbose_name='Nacionalidad')
	ciudad = models.ForeignKey(Ciudad,max_length=5,null=True,blank=True,default=1111,on_delete=models.CASCADE,verbose_name='Ciudad Nacimiento')
	especialidad = models.ForeignKey(Especialidad,max_length=3,null=True,blank=True,default=31,on_delete=models.CASCADE,verbose_name='Especialidad')
	tipo_ter=models.CharField(max_length=10,blank=True,default='',choices=TIPO_TER,verbose_name='Tipo Tercero')
	created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
	updated=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Edición')

	class Meta:
		ordering=["apel1","apel2","nombre1","nombre2"]
		verbose_name='Tercero'
		verbose_name_plural='Terceros'
	
	def __str__(self):
		return str(self.apel1).strip()+" "+str(self.apel2).strip()+" "+str(self.nombre1).strip()+" "+str(self.nombre2).strip()+str(self.razon_social).strip()+"("+str(self.tipo_ter)+")"

 
class Solicitud(models.Model):
	fecha = models.DateField(auto_now_add=True,verbose_name='Fecha Solicitud')
	paciente = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Paciente',related_name="Paciente")
	hospital = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Hospital',related_name="Hospital")
	medico = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Médico',related_name="Médico")
	pagador = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Pagador',related_name="Pagador")
	direccion_envio = models.CharField(max_length=100,blank=True,verbose_name='Dirección de Envio')
	telefono_envio = models.CharField(max_length=35,blank=True,verbose_name='Teléfono de Envio')
	ciudad_envio = models.ForeignKey(CiudadDireccion,default='1112',on_delete=models.CASCADE,verbose_name='Ciudad Envío')
	tipo_cirugia = models.ForeignKey(TipoCirugia,max_length=4,on_delete=models.CASCADE,verbose_name='Tipo Cirugía')
	fecha_cirugia = models.DateField(null=True,blank=True,verbose_name='Fecha Cirugía (dd/mm/aa)')
	id_recibe =  models.CharField(max_length=20,blank=True,verbose_name='Identificación Recibe')
	nombre_recibe = models.CharField(max_length=35,blank=True,verbose_name='Nombre Recibe')
	valortotal = models.DecimalField(max_digits=12,null=True,blank=True,decimal_places=2,default=0,verbose_name='Valor Total')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Edición')
	user = models.CharField(max_length=35,verbose_name='Usuario')
	cerrada = models.BooleanField(default=False)

	class Meta:
		ordering = ['fecha']
		verbose_name='Solicitud'
		verbose_name_plural='Solicitudes'

	    
class SolicitudDetalle(models.Model):
	solicitud = models.ForeignKey(Solicitud,null=False,blank=False,on_delete=models.CASCADE, related_name='solicitud_detalle') 
	tipoinjerto=models.ForeignKey(TipoInjerto,null=False,blank=False,on_delete=models.CASCADE,default='',verbose_name='Tipo de Injerto')
	cantidad=models.PositiveIntegerField(default=1,verbose_name='Cantidad')
	valor=models.DecimalField(max_digits=12,null=False,blank=False,decimal_places=2,default=0,verbose_name='Valor')
	valortotal=models.DecimalField(max_digits=12,null=False,blank=False,decimal_places=2,default=0,verbose_name='Valor Total')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Edición')

	class Meta:
		ordering = ['solicitud']
		verbose_name='Detalle Solicitud'
		verbose_name_plural='Detalle Solicitudes'

class ParametrosSolicitud(models.Model):
	#solicitud = models.ForeignKey(Solicitud,default=0,on_delete=models.CASCADE, related_name='Solcicitud_parametro') 
	paciente = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Paciente',related_name="Paciente_parametro")
	hospital = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Hospital',related_name="Hospital_parametro")
	medico = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Médico',related_name="Médico_parametro")
	pagador = models.ForeignKey(Tercero,on_delete=models.CASCADE,verbose_name='Pagador',related_name="Pagador_parametro")
	user = models.CharField(max_length=35,verbose_name='Usuario')

	class Meta:
		verbose_name='Parametro Solicitud'
		verbose_name_plural='Parametros Solicitudes'

class SolicitudDetalleTemp(models.Model):
	solicitud = models.ForeignKey(Solicitud,default=0,on_delete=models.CASCADE, related_name='solicitud_detalle_temp') 
	#grupoinjerto=models.ForeignKey(Grupo,null=False,blank=False,on_delete=models.CASCADE,default='',verbose_name='Grupo del Injerto')	
	tipoinjerto=models.ForeignKey(TipoInjerto,null=False,blank=False,on_delete=models.CASCADE,default='',verbose_name='Tipo de Injerto')
	cantidad=models.PositiveIntegerField(default=1,verbose_name='Cantidad')
	valor=models.DecimalField(max_digits=12,null=False,blank=False,decimal_places=2,default=0,verbose_name='Valor')
	valortotal=models.DecimalField(max_digits=12,null=False,blank=False,decimal_places=2,default=0,verbose_name='Valor Total')
	user = models.CharField(max_length=35,verbose_name='Usuario')
	
	class Meta:
		ordering = ['solicitud']
		verbose_name='Detalle Solicitud Temporal'
		verbose_name_plural='Detalle Solicitudes Temporal'

	def __str__(self):
		return f'{self.tipoinjerto.descripcion}'