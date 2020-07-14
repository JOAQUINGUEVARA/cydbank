"""cydbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from pages.urls import pages_patterns
#from pedidos.urls import urls
#from profiles.urls import profiles_patterns
from registration.urls import registration_patterns
#from messenger.urls import messenger_patterns
from contact.urls import contact_patterns
from pedidos.urls import pedidos_patterns
from upload.urls import upload_patterns
from chat.urls import chat_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('pages/', include(pages_patterns)),
    #path('profiles/', include(profiles_patterns)),
    path('registration/', include(registration_patterns)),
    #path('messenger/', include(messenger_patterns)),
    path('pedidos/', include(pedidos_patterns)),
    path('contact/', include(contact_patterns)),
    path('upload/', include(upload_patterns)),
    path('chat/', include(chat_patterns)),
    #path('registration/', include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('account/', include('account.urls')),
    #path('accounts/', include('django_registration.backends.activation.urls')),
    #path('accounts/', include('django.contrib.auth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Sitio Administrativo CYDBANK'