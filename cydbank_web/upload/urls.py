from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload import views

upload_patterns = ([
    path('home', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('anexos_identificacion/', views.AnexosIdentificacion,name='anexos_identificacion'),
    path('anexos_formula/', views.AnexosFormula,name='anexos_formula'),
    path('documents/', views.document_list, name='document_list'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    #path('documents/<int:pk>/', views.delete_document, name='delete_document'),
    path('class/document/', views.DocumentListView.as_view(), name='class_document_list'),
    path('class/document/upload/', views.UploadDocumentView.as_view(), name='class_upload_document'),
    path('documents/<int:id>/', views.ListOneDocumentView.as_view(), name='upload_one_document'),
], 'upload')
