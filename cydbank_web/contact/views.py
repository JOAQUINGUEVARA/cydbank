from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.views.generic import TemplateView

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['nombre']
            empresa = form.cleaned_data['empresa']
            cargo = form.cleaned_data['cargo']
            ciudad = form.cleaned_data['ciudad']
            pais = form.cleaned_data['pais']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            message = "Nombre: "+subject+"  Empresa:  "+empresa+"  Cargo: "+cargo+"  Ciudad: "+ciudad+"  País:  "+pais+" Teléfono: "+telefono+"  Mensaje: "+mensaje
            from_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, from_email, [email])
            except BadHeaderError:
                return HttpResponse('Encabezado inválido')
            return redirect('contact:success')
    return render(request, "contact/email.html", {'form': form})


class successView(TemplateView):
    template_name = "contact/gracias.html"