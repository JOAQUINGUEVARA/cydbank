from django.urls import path
from .views import PageDetailView, PageCreate, PageUpdate, PageDelete, MenuPpalView, FAQTitleView, FAQDetailView,VitrinaView,DetalleInjertoView
from .models import Faq

pages_patterns = ([
    path('<int:pk>', PageDetailView.as_view(), name='page'),
    path('create-order/', PageCreate.as_view(), name='create-order'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),

    path('faq_title',FAQTitleView.as_view(), name='faq_title'),
    path('faq_detail/<int:id>/',FAQDetailView.as_view(), name='faq_detail'),

    path('listar_vitrina/<int:id>', VitrinaView.as_view(), name="listar_vitrina"),
    path('detalle_injerto/<int:id>', DetalleInjertoView, name="detalle_injerto"),    
    

], 'pages')