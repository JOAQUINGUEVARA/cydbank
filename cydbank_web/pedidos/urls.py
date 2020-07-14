"""cydpedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pedidos.views import SamplePageView,CrearSolicitudView,CrearMedicoView,CrearPacienteView,CrearHospitalView,CrearPagadorView,ListarPedido,HomePageView,VerPedido,ErrorPageView,ListarPedidoCliente
from pedidos.views import ajax_trae_precio_view,ajax_validar_tercero_view,ListarDetallePedidoView,SumaInjertoView,VerPedidosUnCliente,ListarUnPedidoCliente,SinAnexoMensajeView
from pedidos.views import TercerosSolicitudView,InjertoDeleteView,MostrarInjertosPedidoView,CreaDetallePedidoView,CierraPedidoView,FinalizarPedidoView,MenuUtilitariosView,ListarUltimoPedidoCliente,ImprimirPedidoPDF
from pedidos.views import CrearPacienteFueraView,CrearMedicoFueraView,CrearHospitalFueraView,CrearPagadorFueraView,import_xls_ciudades,import_xls_lista_tecnica,CierrePedidoMensajeView,ajax_add_product,EnvioMailPedido
from django.contrib.auth.decorators import login_required

""" from ajax.views import search """
#CreaDetallePedidoView,

pedidos_patterns = ([
    path('',HomePageView.as_view(), name="homepage" ),
    path('error',ErrorPageView.as_view(), name="error" ),
    
    path('pedidos/', CrearSolicitudView.as_view(), name="crea_pedido"),
    
    path('crear_paciente_fuera/', CrearPacienteFueraView.as_view(), name="crear_paciente_fuera"),
    path('crear_medico_fuera/', CrearMedicoFueraView.as_view(), name="crear_medico_fuera"),
    path('crear_pagador_fuera/', CrearPagadorFueraView.as_view(), name="crear_pagador_fuera"),
    path('crear_hospital_fuera/', CrearHospitalFueraView.as_view(), name="crear_hospital_fuera"),
    
    path('crear_paciente/', CrearPacienteView.as_view(), name="crear_paciente"),
    path('crear_medico/', CrearMedicoView.as_view(), name="crear_medico"),
    path('crear_pagador/', CrearPagadorView.as_view(), name="crear_pagador"),
    path('crear_hospital/', CrearHospitalView.as_view(), name="crear_hospital"),
        
    path('pedidos_tercero/<int:id>/', TercerosSolicitudView.as_view(), name="pedidos_tercero"),
    
    path('ajax/validar_tercero/', ajax_validar_tercero_view, name='validar_tercero'),
    
    path('mostrar_injertos_pedido', MostrarInjertosPedidoView.as_view(), name="mostrar_injertos_pedido"),
    #path('listar_detalle_pedido/',ListarDetallePedidoView.as_view(), name="listar_detalle_pedido"),
    path('crea_detalle_pedido/<int:id>/', CreaDetallePedidoView.as_view(), name="crea_detalle_pedido"),
    path('borra_injerto/<int:pk>/', InjertoDeleteView, name="borra_injerto"),
    path('suma_injerto/<int:id>/', SumaInjertoView.as_view(), name="suma_injerto"),
    path('cierra_pedido', CierraPedidoView, name="cierra_pedido"),
    path('finalizar_pedido/',FinalizarPedidoView.as_view(), name="finalizar_pedido"),
    path('cierre_pedido_mensaje/',CierrePedidoMensajeView.as_view(), name="cierre_pedido_mensaje"),
    path('sin_anexo_mensaje/',SinAnexoMensajeView.as_view(), name="sin_anexo_mensaje"),
    
    path('utilitarios/',MenuUtilitariosView.as_view(), name="utilitarios"),
    #path('export_tercero_file/',ExportTerceroFileView, name='export_tercero_file'),
    #path('export_solicitud_file/',ExportSolicitudFileView, name='export_solicitud_file'),
    #path('export_detalle_solicitud_file/',ExportDetalleSolicitudFileView, name='export_detalle_solicitud_file'),
    
    #path('listar_pedidos/', ListarPedido.as_view(), name="listar_pedidos"),
    #path('listar_ultimo_pedido_cliente', ListarUltimoPedidoCliente, name="listar_ultimo_pedido_cliente"),
    
    path('imprimir_pedido_pdf/<int:id>', ImprimirPedidoPDF, name="imprimir_pedido_pdf"),
    path('listar_pedidos_cliente', ListarPedidoCliente.as_view(), name="listar_pedidos_cliente"),
    path('envio_mail_pedido/<int:id>', EnvioMailPedido, name="envio_mail_pedido"),
    path('ver_pedidos_un_cliente',VerPedidosUnCliente,name="ver_pedidos_un_cliente"),
    path('listar_un_pedido/<int:id>',ListarUnPedidoCliente,name="listar_un_pedido_de_un_cliente"),

    path('ver_pedido/<n_pedido>/<n_precio>/', VerPedido, name="ver_pedido"),
    path('ajax/trae_precio/', ajax_trae_precio_view, name='trae_precio'),
    path('add-product/<int:dk>/', ajax_add_product, name='ajax_add'),

    path('importar_xls_ciudades/', import_xls_ciudades, name="importar_xls_ciudades"),
    path('importar_xls_lista_tecnoca/', import_xls_lista_tecnica, name="importar_xls_lista_tecnica"),

    
],'pedidos')

""" path('pedidos/', CrearPedido.as_view(), name="pedidos"), """
""" path('order-list/', SolicitudListView.as_view(), name='order_list'), """
""" path('pedidos_medico/<int:id>/', CrearSolicitudMedicoView.as_view(), name="pedidos_medico"),
path('pedidos_paciente/<int:id>', CrearSolicitudPacienteView.as_view(), name="pedidos_paciente"),
path('pedidos_hospital/<int:id>/', CrearSolicitudHospitalView.as_view(), name="pedidos_hospital"),
path('pedidos_pagador/<int:id/', CrearSolicitudPagadorView.as_view(), name="pedidos_pagador"), """
""" path('pedidos_tercero/<int:id>', TercerosSolicitudView.as_view(), name="pedidos_paciente"), """