from django.shortcuts import render
from django.views.generic import TemplateView
from pages.models import GrupoPage
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home/home.html"