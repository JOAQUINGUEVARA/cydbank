from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Solicitud,Tercero,SolicitudDetalle,TipoInjerto,ParametrosSolicitud,SolicitudDetalleTemp,Ciudad
from .forms import PacienteForm,HospitalForm,MedicoForm,PagadorForm,PedidoForm
from .tables import InjertosTable,DetallePedidoTable,SolicitudTable,SolicitudTable1,SolicitudDetalleTable,SolicitudesUnClienteTable
from .filters import TipoInjertoFilter

from pages.models import ListaTecnica

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.http import HttpRequest

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

import django_tables2
from django_tables2 import RequestConfig

from django.db.models import Sum
from decimal import Decimal
from django.db import transaction
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime, timezone, date
from django.utils.dateformat import format

from django.template.loader import render_to_string

import xlwt

from .filters import TerceroFilter

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from time import gmtime, strftime
from django.shortcuts import get_object_or_404, redirect, reverse
from .resources  import SolicitudResource
from upload.models import Anexo

from django.core.mail import EmailMessage

from io import StringIO

""" class VitrinaView(ListView):
    template_name = 'pedidos/vitrina.html'
    queryset = TipoInjerto.injertos_activos.all()
    context_object_name = 'injertos'
    paginate_by = 2

class VitrinaHomeView(ListView):
    template_name = 'pedidos/vitrina_home.html'
    queryset =  TipoInjerto.injertos_activos.all()
    context_object_name = 'injertos'
    paginate_by = 2 """

class SuccessMessageMixin:
    success_message = ''

    def get_success_message(self):
        return self.success_message

    def form_valid(self, form):
        messages.success(self.request, self.get_success_message())
        return super().form_valid(form)

class CrearPacienteView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/paciente_form.html'
    form_class = PacienteForm
    success_url = reverse_lazy('pedidos:pedidos_paciente')
    
    def form_valid(self, form):
        tercero = form.save(commit=False)
        tercero.tipo_ter='Paciente'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            parametros = ParametrosSolicitud()
            tercero = Tercero.objects.all().latest('id')
            tercerogen = Tercero.objects.get(identificacion='---')    
            parametros.user = self.request.user.id
            parametros.medico_id = tercerogen.id
            parametros.paciente_id = tercero.id
            parametros.pagador_id = tercerogen.id
            parametros.hospital_id = tercerogen.id
            parametros.save()
            return HttpResponseRedirect(self.get_success_url())    
        else:
            return HttpResponse("No se pudo adicionar,Paciente ya Creado")
        

    def get_success_url(self):
        aa = Tercero.objects.latest('id')
        return reverse_lazy('pedidos:pedidos_tercero',kwargs = {'id': aa.id})

class CrearMedicoView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/medico_form.html'
    form_class = MedicoForm
    success_url = reverse_lazy('pedidos:pedidos_medico')
    
    def form_valid(self, form):
        response = super(CrearMedicoView, self).form_invalid(form)
        tercero = form.save(commit=False)
        tercero.tipo_ter='Medico'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            tercerogen = Tercero.objects.get(identificacion=tercero.identificacion)
            ParametrosSolicitud.objects.filter(user=self.request.user.id).update(medico_id = tercerogen.id)
            return HttpResponseRedirect(self.get_success_url())
        else:
            """ messages.error(self.request,"No se pudo adicionar,Médico ya Creado") """
            success_message = "No se pudo adicionar,Médico ya Creado"
            messages.success(self.request, self.get_success_message())
            return super(SuccessMessageMixin, self).form_valid(form)  # Difference here
            #return response
        

    def get_success_url(self):
        aa = Tercero.objects.latest('id')
        return reverse('pedidos:pedidos_tercero',kwargs = {'id': aa.id})

class CrearHospitalView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/hospital_form.html'
    form_class = HospitalForm
    success_url = reverse_lazy('pedidos:pedidos_hospital')    

    def form_valid(self, form):
        success_message = "Hospital ya Creado"
        tercero = form.save(commit=False)
        tercero.tipo_ter='Hospital'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            tercerogen = Tercero.objects.get(identificacion=tercero.identificacion)
            ParametrosSolicitud.objects.filter(user=self.request.user.id).update(hospital_id = tercerogen.id)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("No se pudo adicionar,Hospital ya Creado")    
        

    def get_success_url(self):
        aa = Tercero.objects.latest('id')
        return reverse('pedidos:pedidos_tercero',kwargs = {'id': aa.id})    

class CrearPagadorView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/pagador_form.html'
    form_class = PagadorForm
    success_url = reverse_lazy('pedidos:pedidos_pagador')

    def form_valid(self, form):
        tercero = form.save(commit=False)
        tercero.tipo_ter='Pagador'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            tercerogen = Tercero.objects.get(identificacion=tercero.identificacion)
            ParametrosSolicitud.objects.filter(user=self.request.user.id).update(pagador_id = tercerogen.id)
            return HttpResponseRedirect(self.get_success_url())
        else:
           return HttpResponse("No se pudo adicionar,Pagador ya Creado")
       
        def get_success_url(self):
            aa = Tercero.objects.latest('id')
            return reverse('pedidos:pedidos_tercero',kwargs = {'id': aa.id})

class CrearMedicoFueraView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/medico_form.html'
    form_class = MedicoForm
    success_url = reverse_lazy('pedidos:homepage')
    
    def get_success_url(self):
        return reverse('pedidos:homepage')

    def form_valid(self, form):
        tercero = form.save(commit=False)
        tercero.tipo_ter='Medico'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            return HttpResponseRedirect(self.get_success_url())    
        else:
            return HttpResponse("No se pudo adicionar,Médico ya Creado")
        
class CrearHospitalFueraView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/hospital_form.html'
    form_class = HospitalForm
    success_url = reverse_lazy('pedidos:homepage')    

    def get_success_url(self):
        return reverse('pedidos:homepage')

    def form_valid(self, form):
        success_message = "Hospital ya Creado"
        tercero = form.save(commit=False)
        tercero.tipo_ter='Hospital'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            return HttpResponseRedirect(self.get_success_url())    
        else:
            return HttpResponse("No se pudo adicionar,Hospital ya Creado")
        
class CrearPacienteFueraView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/paciente_form.html'
    form_class = PacienteForm
    success_url = reverse_lazy('pedidos:homepage')

    def get_success_url(self):
        return reverse('pedidos:homepage')

    def form_valid(self, form):
        tercero = form.save(commit=False)
        tercero.tipo_ter='Paciente'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("No se pudo adicionar,Paciente ya Creado") 

class CrearPagadorFueraView(SuccessMessageMixin,CreateView):
    model = Tercero
    template_name = 'pedidos/pagador_form.html'
    form_class = PagadorForm
    success_url = reverse_lazy('pedidos:homepage')

    def get_success_url(self):
        return reverse('pedidos:homepage')

    def form_valid(self, form):
        tercero = form.save(commit=False)
        tercero.tipo_ter='Pagador'
        if  Tercero.objects.filter(identificacion=tercero.identificacion).count() == 0:
            tercero.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("No se pudo adicionar,Pagador ya Creado")
        

def VerPedido(request,n_pedido,n_precio):
    dvalor=float(00.00)
    dvalor=Precios.objects.get(pk=n_precio)
    dcantidad=int()
    dcantidad=Solicitud_detalle.objects.get(pk=n_pedido)
    Solicitud_detalle.objects.filter(pk=n_pedido).update(valortotal=float(dvalor)*float(dcantidad))
    datos_cabeza=get_object_or_404(Solicitud,pk=n_pedido)
    datos_cuerpo=get_object_or_404(Solicitud_detalle,pk=n_pedido)
    return render_to_response('pedidos/solicitudes_listado.html',{'solicitud:':datos_cabeza,'solicitud_detalle:':datos_cuerpo},context_instance=RequestContext(request))

 
class ListarPedido(ListView):
    template_name = 'pedidos/solicitudes_listado.html'
    model = Solicitud
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kargs)
        return context

class ListarPedidoCliente(ListView):
    template_name = 'pedidos/solicitudes_listado.html'
    
    def get_queryset(self):
        return   SolicitudDetalle.objects.filter(numero=self.lnumero)
    
    def get_context_data(self, *args, **kwargs):
        cabeza = Solicitud.objects.filter(id=self.kwargs['lnumero'])
        cuerpo = SolicitudDetalle.objects.filter(solicitud_id=self.kwargs['lnumero'])
        return {'cabeza': cabeza, 'cuerpo': cuerpo}



""" class ListarUltimoPedidoCliente(ListView):
    template_name = 'pedidos/solicitudes_listado.html'
    
    def get(self, request, *args, **kwargs):
        cabeza = Solicitud.objects.filter(user=self.request.user.id).latest('id')
        cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
        context = {'cabeza': cabeza,'cuerpo': cuerpo}
        print(context)
        return render(request, self.template_name, context=context) """


def  ListarUltimoPedidoCliente(request):
    Solicitud.objects.filter(user=request.user.id).latest('id')
    cabeza = Solicitud.objects.filter(user=request.user.id).latest('id')
    cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
    total_pedido = cuerpo.aggregate(Sum('valortotal'))['valortotal__sum']
    total_pedido = f'{total_pedido}'
    total = total_pedido
    return render(request,'pedidos/solicitudes_listado.html',context={'cabeza':cabeza,'cuerpo':cuerpo,'total':total})


def VerPedidosUnCliente(request):
    table =SolicitudesUnClienteTable(Solicitud.objects.filter(user=request.user.id).order_by('-created' ))
    table.paginate(page=request.GET.get("page", 1), per_page=8)
    solicitudes = Solicitud.objects.filter(user=request.user.id)
    total_pedido = solicitudes.aggregate(Sum('valortotal'))['valortotal__sum']
    total_pedido = f'{total_pedido}'
    total = total_pedido
    return render(request,'pedidos/solicitudes_un_cliente.html',context={'table':table,'total':total})

def ListarUnPedidoCliente(request,id):
    cabeza = Solicitud.objects.get(pk=id)
    cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
    total_pedido = cuerpo.aggregate(Sum('valortotal'))['valortotal__sum']
    total_pedido = f'{total_pedido}'
    total = total_pedido
    return render(request,'pedidos/solicitudes_listado.html',context={'cabeza':cabeza,'cuerpo':cuerpo,'total':total})

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.lib.pagesizes import A4 
from reportlab.lib.units import inch, cm
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

def cabecera(pdf,id):
    #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
    archivo_imagen = settings.MEDIA_ROOT+'/img/logo_cyd.png'
    #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
    pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)

    #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
    pdf.setFont("Helvetica", 16)
    #Dibujamos una cadena en la ubicación X,Y especificada
    y = 770

    pdf.drawString(170, y, u"FUNDACION COSME Y DAMIAN")
    pdf.setFont("Helvetica", 14)
    y -= 20
    pdf.drawString(200, y, u"SOLICITUD DE INJERTOS")    
    pdf.setFont("Helvetica", 9)    
    cabeza = Solicitud.objects.get(id=id)
    #cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
    
    x = 570
    factor = 15
    baja = 5
    y -= 10
    pdf.line(30,y,x,y)
    y -= baja+5 
    pdf.drawString(30,y , u"Número : "+str(cabeza.id))
    pdf.drawString(180,y , u"Fecha : "+cabeza.created.strftime("%Y-%m-%d %H:%M:%S"))
    y -= baja
    
    pdf.line(30,y,x,y)
    y -= baja
    y -= factor
    pdf.drawString(30, y, u"Paciente : "+str(cabeza.paciente))
    y -= factor
    pdf.drawString(30, y, u"Médico   : "+str(cabeza.medico))
    y -= factor
    pdf.drawString(30, y, u"Hospital : "+str(cabeza.hospital))
    y -= factor
    pdf.drawString(30, y, u"Pagador  : "+str(cabeza.pagador))
    y -= baja
    pdf.line(30,y,x,y)
    y -= baja
    y -= factor
    pdf.drawString(30, y, u"Tipo Cirugía : "+str(cabeza.tipo_cirugia))
    y -= factor
    pdf.drawString(30, y, u"Fecha Cirugía : "+str(cabeza.fecha_cirugia)) 
    #y -= factor
    y -= baja
    pdf.line(30,y,x,y)
    y -= baja
    y -= factor
    pdf.drawString(30, y, u"Id. Recibe        : "+str(cabeza.id_recibe))
    y -= factor
    pdf.drawString(30, y, u"Nombre Recibe     : "+str(cabeza.nombre_recibe))
    y -= factor
    pdf.drawString(30, y, u"Dirección Envío   : "+str(cabeza.direccion_envio))
    y -= factor
    pdf.drawString(30, y, u"Teléfono Envío    : "+str(cabeza.telefono_envio))
    y -= factor
    pdf.drawString(30, y, u"Ciudad Envío      : "+str(cabeza.ciudad_envio))
    y -= baja
    pdf.line(30,y,560,y)
    y -= baja

def tabla(pdf,y,id):
    print(y)
    cuerpo = SolicitudDetalle.objects.filter(solicitud_id=id)
    total_pedido = cuerpo.aggregate(Sum('valortotal'))['valortotal__sum']
    #total_pedido = f'{total_pedido}'
    total = total_pedido
    #Creamos una tupla de encabezados para neustra tabla
    encabezados = ('Tipo Injerto', 'Cantidad', 'Valor Unit.', 'Valor Total')
    #Creamos una lista de tuplas que van a contener a las personas
    detalles = [(cuerpo.tipoinjerto, cuerpo.cantidad, '{:,}'.format(cuerpo.valor), '{:,}'.format(cuerpo.valortotal)) for cuerpo in cuerpo]
    #Establecemos el tamaño de cada una de las columnas de la tabla
    detalle_orden = Table([encabezados] + detalles, colWidths=[12 * cm, 2 * cm, 2.5 * cm, 2.5 * cm])
    #Aplicamos estilos a las celdas de la tabla
    detalle_orden.setStyle(TableStyle(
        [
            #La primera fila(encabezados) va a estar centrada
            ('ALIGN',(0,0),(3,0),'CENTER'),
            #Los bordes de todas las celdas serán de color negro y con un grosor de 1
            ('GRID', (0, 0), (-1, -1), 1, colors.black), 
            #El tamaño de las letras de cada una de las celdas será de 10
            ('FONTSIZE', (0, 0), (-1, -1), 7),
        ]
    ))
    # Restamos a y por cada fila de la frid
    for a in cuerpo:
        y -= 5
    # Descontamos el encabezado
    #Establecemos el tamaño de la hoja que ocupará la tabla 
    detalle_orden.wrapOn(pdf, 500, 800)
    #Definimos la coordenada donde se dibujará la tabla
    detalle_orden.drawOn(pdf, 30,y)
    #stotal = format(total_pedido,',d')
    #print(stotal)
    y -= 10
    pdf.drawString(430, y, u"Total Pedido      : "+('{:,}'.format(total_pedido)+'.00'))


def ImprimirPedidoPDFMail(request,id):
    y = 0
    cabeza = Solicitud.objects.filter(id=id)
    #cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
    #Indicamos el tipo de contenido a devolver, en este caso un pdf
    response = HttpResponse(content_type='application/pdf')
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer)
    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
    cabecera(pdf,id)
    #Con show page hacemos un corte de página para pasar a la siguiente
    y = 455
    tabla(pdf,y,id)
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue() 
    return pdf

def ImprimirPedidoPDF(request,id):  
    y = 0
    cabeza = Solicitud.objects.filter(id=id)
    #cuerpo = SolicitudDetalle.objects.filter(solicitud_id=cabeza.id)
    #Indicamos el tipo de contenido a devolver, en este caso un pdf
    response = HttpResponse(content_type='application/pdf')
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer)
    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
    cabecera(pdf,id)
    #Con show page hacemos un corte de página para pasar a la siguiente
    y = 455
    tabla(pdf,y,id)
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response


class CierrePedidoMensajeView(TemplateView):
    template_name = "pedidos/cierre_pedido_mensaje.html"

class SinAnexoMensajeView(TemplateView):
    template_name = "pedidos/sin_anexo_mensaje.html"

class HomePageView(TemplateView):
    template_name = "pedidos/home_pedidos.html"

    def get_context_data(self, **kwargs):
        context = super( HomePageView, self).get_context_data(**kwargs)
        context['user'] = request.user.name
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Fundaciòn Cosme y Damian"})
        
class ErrorPageView(TemplateView):
    template_name = "pedidos/error.html"

class SamplePageView(TemplateView):
    template_name = "pedidos/sample.html"
    
    def home(self,request):
        return render(request,"pedidos/home.html")   

def ajax_trae_precio_view(request):
    precio = request.GET.get('tipoinjerto', None)
    aa = Tipoinjerto.objects.get(pk=tipoinjerto)
    precio=aa.valor
    data={'precio':precio}
    return JsonResponse(data)

def ajax_validar_tercero_view(request):
    identificacion = request.GET.get('identificacion', None)
    data = {
        'is_taken': Tercero.objects.filter(identificacion__iexact=identificacion).exists()
    }
    return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
class CrearSolicitudView(CreateView):
    template_name = 'pedidos/solicitudes.html'
    form_class = PedidoForm
    model = Solicitud
    
    def get_initial(self,*args,**kwargs):
        # Cargo solicitud de temporales si está pendiente    
        #SolicitudDetalleTemp.objects.filter(user=self.request.user.id).delete()
        initial=super(CrearSolicitudView,self).get_initial(**kwargs)
        """ if Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).exists():
            solicitud = Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).latest('id')
            #idinj = solicituddetalle_ult_doc.tipoinjerto_id
            #print (solicitud_pend.id)
            #solicitud = Solicitud.objects.get(id=solicitud_pend.id)
            initial['paciente'] = solicitud.paciente_id
            initial['medico'] = solicitud.medico_id
            initial['hospital'] = solicitud.hospital_id
            initial['pagador'] = solicitud.pagador_id
            initial['fecha'] = solicitud.fecha
            initial['direccion_envio'] = solicitud.direccion_envio
            initial['telefono_envio'] = solicitud.telefono_envio
            initial['fecha_cirugia'] = solicitud.fecha_cirugia
            initial['ciudad_envio'] = solicitud.ciudad_envio_id
            if solicitud.ciudad_envio_id == '' :
                initial['ciudad_envio'] = '1112'
            initial['tipo_cirugia'] = solicitud.tipo_cirugia_id
            initial['id_recibe'] = solicitud.id_recibe
            initial['nombre_recibe'] = solicitud.nombre_recibe
            initial['id'] = solicitud.id
        else: """
        initial['ciudad_envio'] = '1112'

        return initial
         
    def get_success_url(self):
        #return reverse('invite_list_own', args=[self.request.tenant.slug])
        #ParametrosSolicitud.objects.filter(user=self.request.user.id).delete()
        return reverse_lazy('pedidos:mostrar_injertos_pedido')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user.id
            self.cerrada = False
            self.object.save()
            solicitud = Solicitud.objects.latest('id')
            """ if solicitud.user == '':
                Solicitud.objects.get(id=solictud.id).update(user = self.request.user.id)  """
            ParametrosSolicitud.objects.filter(user=self.request.user.id).delete()
        else:
            return render(request, "error_message.html", {'form': messageForm})    
        return HttpResponseRedirect(self.get_success_url()) 


class TercerosSolicitudView(CreateView):
    template_name = 'pedidos/solicitudes.html'
    form_class = PedidoForm
    model = Solicitud
    success_url = reverse_lazy('pedidos:mostrar_injertos_pedido')
    
    def get_initial(self,*args,**kwargs):
        initial=super(TercerosSolicitudView,self).get_initial(**kwargs)
        if ParametrosSolicitud.objects.filter(user=self.request.user.id).exists():
            tt = ParametrosSolicitud.objects.filter(user=self.request.user.id).count()
            if tt == 1 :
                parametros = ParametrosSolicitud.objects.get(user=self.request.user.id)
                initial['paciente']=parametros.paciente_id
                initial['medico']=parametros.medico_id
                initial['hospital']=parametros.hospital_id
                initial['pagador']=parametros.pagador_id
            else:
                parametros = ParametrosSolicitud.objects.filter(user=self.request.user.id).latest('id')
                initial['paciente']=parametros.paciente_id
                initial['medico']=parametros.medico_id
                initial['hospital']=parametros.hospital_id
                initial['pagador']=parametros.pagador_id    
        return initial

class  MostrarInjertosPedidoView(TemplateView):
    template_name = "pedidos/injertos_solicitud.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        return TipoInjerto.injertos_activos.all()
        #return TipoInjerto.objects.all()

    def get_context_data(self, **kwargs):
        context = super( MostrarInjertosPedidoView, self).get_context_data(**kwargs)
        filter = TipoInjertoFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        table = InjertosTable(filter.qs)
        table.paginate(page=self.request.GET.get("page", 1), per_page=10)
        detalle = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id))
        context['filter'] = filter
        context['table'] = table
        orders = SolicitudDetalleTemp.objects.filter(user=self.request.user.id)
        total_pedido = 0
        data = dict()
        total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
        total_pedido = f'{total_pedido}'
        context['detalle'] = detalle
        context['total'] = total_pedido
        if Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).exists():
            solicitud = Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).latest('id')
            context['solicitud_no'] = solicitud.id
        return context

class SumaInjertoView(TemplateView):
    template_name = "pedidos/injertos_solicitud.html"
    
    def get_query_set(self,*args,**kwargs):
        return TipoInjerto.injertos_activos.all()
        
    def get_context_data(self,*args,**kwargs):
        if  SolicitudDetalleTemp.objects.filter(user=self.request.user.id).exists():
            id = self.kwargs.get('id')
            solicituddetalle = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).get(id=id)
            idinj = solicituddetalle.tipoinjerto_id
            #solicituddetalle = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).get(tipoinjerto_id=idinj)
            precio = solicituddetalle.valor
            lcantidad = solicituddetalle.cantidad
            lcantidad += 1
            ltotal =precio * lcantidad
            SolicitudDetalleTemp.objects.filter(tipoinjerto_id=idinj).filter(user=self.request.user.id).update(cantidad=lcantidad,valortotal=ltotal)
        detalle = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id))     
        context = super(SumaInjertoView, self).get_context_data(**kwargs)
        filter = TipoInjertoFilter(self.request.GET, queryset=self.get_query_set(**kwargs))       
        lfilter = filter
        orders = SolicitudDetalleTemp.objects.filter(user=self.request.user.id)
        table = InjertosTable(filter.qs)
        table.paginate(page=self.request.GET.get("page", 1), per_page=10)
        total_pedido = 0
        #data = dict()
        total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
        total_pedido = f'{total_pedido}'
        context['filter'] = filter
        context['detalle'] = detalle
        context['total'] = total_pedido
        context['table'] = table
        print(context)
        return context


def ajax_add_product(request, dk):
    product = get_object_or_404(TipoInjerto, id=dk)
    print(product)
    if  SolicitudDetalleTemp.objects.filter(user=request.user.id).filter(tipoinjerto_id=product).exists():
        solicituddetalle = SolicitudDetalleTemp.objects.filter(user=request.user.id).filter(tipoinjerto_id=dk).latest('id')
        instance = solicituddetalle
        precio = solicituddetalle.valor
        lcantidad = solicituddetalle.cantidad
        lcantidad += 1
        ltotal =precio * lcantidad
        SolicitudDetalleTemp.objects.filter(tipoinjerto_id=dk).filter(user=request.user.id).update(cantidad=lcantidad,valortotal=ltotal)        
    else:
        precio = product.valor
        cantidad = 1
        solicituddetalle =SolicitudDetalleTemp()
        instance = solicituddetalle
        solicituddetalle.tipoinjerto_id = dk
        solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
        # Recupero el número de la ultima solicitud del usuario
        solicituddetalle.solicitud_id = solicitud.id
        solicituddetalle.cantidad = cantidad
        solicituddetalle.valor = precio
        solicituddetalle.valortotal = precio * cantidad
        solicituddetalle.user = request.user.id
        solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
        solicituddetalle.solicitud_id = solicitud.id        
        solicituddetalle.save()
    tables = [    
    InjertosTable(TipoInjerto.injertos_activos.all()),
    DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=request.user.id))
    ]
    detalle = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=request.user.id))
    filter = TipoInjertoFilter(request.GET)
    table = InjertosTable(filter.qs)
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    orders = SolicitudDetalleTemp.objects.filter(user=request.user.id)
    total_pedido = 0
    total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
    total_pedido = f'{total_pedido}'
    return redirect(reverse('pedidos:mostrar_injertos_pedido'))



class CreaDetallePedidoView(TemplateView):
    template_name = "pedidos/injertos_solicitud.html"
    paginate_by = 10
   
    def get_success_url(self):
        sol = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).latest('id')
        id = sol.id
        return reverse_lazy('pedidos:mostrar_injertos_pedido')

    def get_success_message(self, cleaned_data):
        return self.success_message

    def get_query_set(self,*args,**kwargs):
        #return TipoInjerto.objects.all()    
        return TipoInjerto.injertos_activos.all()
    
    def get_context_data(self,*args,**kwargs):
        idinj = self.kwargs.get('id')        
       
        aa = TipoInjerto.injertos_activos.get(id=idinj)
        #aa = TipoInjerto.objects.get(id=idinj)
        if  SolicitudDetalleTemp.objects.filter(user=self.request.user.id).filter(tipoinjerto_id=idinj).exists():
            #solicituddetalle_ult_doc = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).latest('id')
            #idinj_ult = solicituddetalle_ult_doc.tipoinjerto_id
            # Recupero la cantidad anterior
            solicituddetalle = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).filter(tipoinjerto_id=idinj).latest('id')
            precio = solicituddetalle.valor
            lcantidad = solicituddetalle.cantidad
            lcantidad += 1
            ltotal =precio * lcantidad
            #SolicitudDetalleTemp.objects.filter(user=self.request.user.id).filter(tipoinjerto_id=idinj).update(cantidad=lcantidad, precio=lprecio)
            # Actualizamos la cantida del injerto y el valor total
            SolicitudDetalleTemp.objects.filter(tipoinjerto_id=idinj).filter(user=self.request.user.id).update(cantidad=lcantidad,valortotal=ltotal)
        else:
            precio = aa.valor
            cantidad = 1
            solicituddetalle =SolicitudDetalleTemp()
            solicituddetalle.tipoinjerto_id = idinj
            solicitud = Solicitud.objects.filter(user=self.request.user.id).latest('id')
            # Recupero el número de la ultima solicitud del usuario
            solicituddetalle.solicitud_id = solicitud.id
            solicituddetalle.cantidad = cantidad
            solicituddetalle.valor = precio
            solicituddetalle.valortotal = precio * cantidad
            solicituddetalle.user = self.request.user.id
            solicitud = Solicitud.objects.filter(user=self.request.user.id).latest('id')
            solicituddetalle.solicitud_id = solicitud.id
            #Si hay solicitudes detalle creadas
            #sw = 0
            solicituddetalle.save()
        tables = [
        InjertosTable(TipoInjerto.injertos_activos.all()),
        DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id))
        ]
        detalle = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id))
        context = super( CreaDetallePedidoView, self).get_context_data(**kwargs)
        filter = TipoInjertoFilter(self.request.GET, queryset=self.get_query_set(**kwargs))
        table = InjertosTable(filter.qs)
        #table = InjertosTable(TipoInjerto.injertos_activos.all())
        table.paginate(page=self.request.GET.get("page", 1), per_page=10)
        context['filter'] = filter
        context['table'] = table
        orders = SolicitudDetalleTemp.objects.filter(user=self.request.user.id)
        total_pedido = 0
        total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
        total_pedido = f'{total_pedido}'
        context['detalle'] = detalle
        context['total'] = total_pedido
        return context

class FinalizarPedidoView(TemplateView):
    template_name = "pedidos/detalle_solicitud_final.html"

    def get_queryset(self, **kwargs):
        return TipoInjerto.injertos_activos.all()
        #return TipoInjerto.objects.all()

    def get_context_data(self, **kwargs):
        #id = self.kwargs('id')
        table=DetallePedidoTable(SolicitudDetalleTemp.objects.all())
        context = super( FinalizarPedidoView, self).get_context_data(**kwargs)
        if SolicitudDetalleTemp.objects.filter(user=self.request.user.id).count()>0:
            solicituddetalle = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).latest('id')
            id = solicituddetalle.solicitud_id
            table = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id).filter(solicitud_id=id))
            #RequestConfig(self.request).configure(table)
            solicitud =  SolicitudTable(Solicitud.objects.filter(id=id))
            if SolicitudDetalleTemp.objects.filter(user=self.request.user.id).count()>0:
                orders = SolicitudDetalleTemp.objects.filter(user=self.request.user.id)
                total_pedido = 0
                data = dict()
                total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
                total_pedido = f'{total_pedido}'
                context = {'table':table,'total':total_pedido,'solicitud':solicitud}
            else:
                context={'table':table,'solicitud':solicitud}
        else:
            context={'table':table} 
        return context        

class  ListarDetallePedidoView(TemplateView):
    template_name = "pedidos/detalle_solicitud.html"

    def get_queryset(self, **kwargs):
        return TipoInjerto.objects.all()

    def get_context_data(self, **kwargs):
        #id = self.kwargs('id')
        table=DetallePedidoTable(SolicitudDetalleTemp.objects.all())
        context = super( ListarDetallePedidoView, self).get_context_data(**kwargs)
        if SolicitudDetalleTemp.objects.filter(user=self.request.user.id).count()>0:
            solicituddetalle = SolicitudDetalleTemp.objects.filter(user=self.request.user.id).latest('id')
            id = solicituddetalle.solicitud_id
            table = DetallePedidoTable(SolicitudDetalleTemp.objects.filter(user=self.request.user.id).filter(solicitud_id=id))
            #RequestConfig(self.request).configure(table)
            if SolicitudDetalleTemp.objects.filter(user=self.request.user.id).count()>0:
                orders = SolicitudDetalleTemp.objects.filter(user=self.request.user.id)
                total_pedido = 0
                data = dict()
                total_pedido = orders.aggregate(Sum('valortotal'))['valortotal__sum']
                total_pedido = f'{total_pedido}'
                context = {'table':table,'total':total_pedido}
            else:
                context={'table':table}
        else:
            context={'table':table} 
        return context

def InjertoDeleteView(request,pk):
    id = pk
    solicituddetalle_ult_doc = SolicitudDetalleTemp.objects.get(pk=id)
    # Recupero la cantidad anterior
    cantidad = solicituddetalle_ult_doc.cantidad
    precio = solicituddetalle_ult_doc.valor
    idinj = solicituddetalle_ult_doc.tipoinjerto_id
    if  cantidad > 0 :
        cantidad -= 1
        total =precio * cantidad
        # Actualizamos la cantida del injerto y el valor total
        if cantidad >0:
            SolicitudDetalleTemp.objects.filter(tipoinjerto_id=idinj).filter(user=request.user.id).update(cantidad=cantidad,valortotal=total)
        else:
            SolicitudDetalleTemp.objects.get(pk=id).delete()    
    else:
        SolicitudDetalleTemp.objects.get(pk=id).delete()
    return redirect('pedidos:mostrar_injertos_pedido')

def CierraPedidoView(request):
    solicituddetalletemp = SolicitudDetalleTemp.objects.filter(user=request.user.id)
    #solicitud = solicituddetalletemp.solicitud_id
    solicitud = Solicitud.objects.filter(user=request.user.id).filter(cerrada=False).latest('id')
    no_solicitud=solicitud.id
    sigue  = False 
    anexo1 = False
    anexo2 = False
    if Anexo.objects.filter(idsolicitud_id = solicitud.id).exists():
        anexo = Anexo.objects.filter(idsolicitud_id = solicitud.id)  
        for i in anexo:
            if i.idanexo_id == 1:
                anexo1 = True
                sigue = True
            else:
                sigue = False    
            if i.idanexo_id == 2:
                anexo2 = True
                sigue = True
            else:
                sigue = False    
    if anexo1 and anexo2:
       sigue == True      
    if sigue:
        #print(solicituddetalletemp)
        total_pedido=0
        #no_solicitud = 0
        for i in solicituddetalletemp:
            if SolicitudDetalle.objects.count()>0:
                solicituddetalle = SolicitudDetalle.objects.latest('id')
                solicituddetalle.id = solicituddetalle.id+1
                #solicituddetalle.solicitud_id = 4
            else:
                solicituddetalle = SolicitudDetalle()
                solicituddetalle.id = 1
            #no_solicitud = i.solicitud_id
            total_pedido += i.valortotal    
            #solicituddetalletemp = SolicitudDetalleTemp.objects.filter(user=request.user.id).get(pk=i.id)
            solicituddetalle.solicitud_id = no_solicitud
            solicituddetalle.tipoinjerto_id = i.tipoinjerto_id
            solicituddetalle.valor = i.valor
            solicituddetalle.cantidad = i.cantidad
            solicituddetalle.valortotal = i.valortotal
            solicituddetalle.user = request.user.id
            solicituddetalle.save()
        Solicitud.objects.filter(id=no_solicitud).update(cerrada= True,valortotal = total_pedido)
        SolicitudDetalleTemp.objects.filter(user=request.user.id).delete()
        return redirect('pedidos:envio_mail_pedido',no_solicitud)
    else:
        return redirect('pedidos:sin_anexo_mensaje')

from .forms import AnexosForm
import os


def EnvioMailPedido(request,id):
    anexos = Anexo.objects.filter(idsolicitud=id)
    solicitante = request.user.username
    #listamail=['odontologia@cydbank.org','atencionalpaciente@cydbank.org','ortopedia@cydbank.org']
    listamail=['jjguevara_a@hotmail.com']
    destinatarios = listamail
    email = request.user.email
    subject ="Solicitante: "+solicitante+"  Solicitud No.: "+str(id)+" Email:  "+email+" Hora: "+strftime("%Y-%m-%d %H:%M:%S", gmtime())
    message = "Solicitud Web"     
    from_email = settings.EMAIL_HOST_USER
    message = "Solicitud web "
    #listamail=['odontologia@cydbank.org','atencionalpaciente@cydbank.org','ortopedia@cydbank.org']
    listamail=['jjguevara_a@hotmail.com']
    destinatarios = listamail
    mail = EmailMessage(
            subject,
            message,
            from_email,
            to=None,
            bcc=destinatarios,
    )
    i = 1
    for anexo in anexos:
        ruta_prog = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_prog += '/media/'
        ruta_archivo = os.path.join(ruta_prog, str(anexo.archivo))
        if i == 1:
            filename = 'Identificacion_'+solicitante
        else:
            filename = 'Formula_'+solicitante   
        mail.attach_file(ruta_archivo)
    
    ##################################################
    solicitud = Solicitud.objects.get(id=id)
    
    pdf = ImprimirPedidoPDFMail(request,solicitud.id)
    mail.attach('pedido.pdf', pdf, 'application/pdf')
    
    import csv
    
    q1 = Tercero.objects.filter(identificacion=solicitud.paciente.identificacion).select_related()
    q2 = Tercero.objects.filter(identificacion=solicitud.medico.identificacion).select_related()
    q3 = Tercero.objects.filter(identificacion=solicitud.hospital.identificacion).select_related()
    q4 = Tercero.objects.filter(identificacion=solicitud.pagador.identificacion).select_related()
    csvfile=StringIO()
    csvwriter =csv.writer(csvfile)
    for tercero in q1:
            csvwriter.writerow([tercero.id,tercero.identificacion,tercero.tipoidentificacion.idtipoidentifica,tercero.nombre1,tercero.nombre2,tercero.apel1,tercero.apel2,
            tercero.razon_social,tercero.direccion,tercero.ciudad_direccion.idciudad,tercero.telefono,tercero.email,tercero.eps.ideps,
            tercero.plan_salud.idplan,tercero.fecha_nacimiento,tercero.ciudad.idciudad,tercero.especialidad.idespecial,tercero.tipo_ter])
    for tercero in q2:
            csvwriter.writerow([tercero.id,tercero.identificacion,tercero.tipoidentificacion.idtipoidentifica,tercero.nombre1,tercero.nombre2,tercero.apel1,tercero.apel2,
            tercero.razon_social,tercero.direccion,tercero.ciudad_direccion.idciudad,tercero.telefono,tercero.email,tercero.eps.ideps,
            tercero.plan_salud.idplan,tercero.fecha_nacimiento,tercero.ciudad.idciudad,tercero.especialidad.idespecial,tercero.tipo_ter])
    for tercero in q3:
            csvwriter.writerow([tercero.id,tercero.identificacion,tercero.tipoidentificacion.idtipoidentifica,tercero.nombre1,tercero.nombre2,tercero.apel1,tercero.apel2,
            tercero.razon_social,tercero.direccion,tercero.ciudad_direccion.idciudad,tercero.telefono,tercero.email,tercero.eps.ideps,
            tercero.plan_salud.idplan,tercero.fecha_nacimiento,tercero.ciudad.idciudad,tercero.especialidad.idespecial,tercero.tipo_ter])
    for tercero in q4:
            csvwriter.writerow([tercero.id,tercero.identificacion,tercero.tipoidentificacion.idtipoidentifica,tercero.nombre1,tercero.nombre2,tercero.apel1,tercero.apel2,
            tercero.razon_social,tercero.direccion,tercero.ciudad_direccion.idciudad,tercero.telefono,tercero.email,tercero.eps.ideps,
            tercero.plan_salud,tercero.fecha_nacimiento,tercero.ciudad.idciudad,tercero.especialidad.idespecial,tercero.tipo_ter])
    mail.attach('tercero.csv', csvfile.getvalue(), 'text/csv')            
    
    csvfile=StringIO()
    csvwriter =csv.writer(csvfile)

    solicitud = Solicitud.objects.get(id=id)

    csvwriter.writerow([solicitud.id,solicitud.fecha,solicitud.paciente_id,solicitud.hospital_id,solicitud.medico_id,solicitud.pagador_id,
    solicitud.direccion_envio,solicitud.telefono_envio,solicitud.ciudad_envio_id,solicitud.tipo_cirugia_id,solicitud.fecha_cirugia,
    solicitud.valortotal,])
    
    mail.attach('solicitud.csv', csvfile.getvalue(), 'text/csv')
    
    csvfile=StringIO()
    csvwriter =csv.writer(csvfile)

    solicitud_detalle = SolicitudDetalle.objects.filter(solicitud_id=id)
    for solicituddetalle in solicitud_detalle:
        csvwriter.writerow([solicituddetalle.tipoinjerto_id,solicituddetalle.cantidad,solicituddetalle.valor,solicituddetalle.valortotal])
    
    mail.attach('solicitud_detalle.csv', csvfile.getvalue(), 'text/csv')
    
    
    #response.write(pdf)
    #return response

    #doc.build(Document)
    #pdf = buffer.getvalue()
    #buffer.close()

    #pdf.showPage()
    #pdf.save()
    #pdf = buffer.getvalue()
    #buffer.close()

    #return pdf
    
    #mail.attach('pedido.pdf', pdf, 'application/pdf')

    mail.send()
    
    return redirect('pedidos:cierre_pedido_mensaje')

 
    
class MenuUtilitariosView(TemplateView):
    template_name = "pedidos/menu_utilitarios.html"


def import_xls_ciudades(request):
    if "GET" == request.method:
        return render(request, 'pedidos/import_xls_ciudades.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        print(excel_file)
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["DATOS"]
        print(worksheet)
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        f = Ciudad()
        """ for row in worksheet.iter_rows(): """
        r=0
        for row in excel_data:
            print(row)
            f.idciudad = row[0]
            if Ciudad.objects.filter(idciudad=f.idciudad).count() == 0:
                
                f.departamento_id = row[1]
                f.pais_id = row[2]
                f.descripcion = row[3]
                
                if len(str(f.idciudad)) == 4 :
                    f.idciudad = '0'+str(f.idciudad)    
                else:
                    f.idciudad = str(f.idciudad)
                f.departamento_id = str(f.departamento_id)
                f.pais_id = str(f.pais_id)
                f.id = r
                print(f.idciudad)
                print(f.departamento_id)
                print(f.pais_id)
                f.save()
                r = r+1        
        return render(request, 'pedidos/import_xls.html', {"excel_data":excel_data})

def import_xls_lista_tecnica(request):
    if "GET" == request.method:
        return render(request, 'pedidos/import_xls_lista_tecnica.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        print(excel_file)
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["DATOS"]
        print(worksheet)
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        f = ListaTecnica()
        """ for row in worksheet.iter_rows(): """
        r=0
        for row in excel_data:
            print(row)
                  
            f.descripcion = row[0]
            f.proceso = row[1]
            f.image = row[2]
            f.cirugia = row[3]
            f.grupo_id = row[4]
                       
            f.id = r
            print(f.descripcion)
            print(f.proceso)
            print(f.cirugia)
            print(f.image)
            print(f.grupo_id)
            f.save()
            r = r+1        
        return render(request, 'pedidos/import_xls.html', {"excel_data":excel_data})    