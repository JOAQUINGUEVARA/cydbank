
from django.contrib import admin
from django.urls import path

from .views import emailView, successView

contact_patterns = ([
    path('contact/', emailView, name='contact'),
    path('success/', successView.as_view(), name='success'),
], 'contact')