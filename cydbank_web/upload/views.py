from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import View

from .forms import DocumentForm
from .models import Document

from django.contrib import messages 
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect
 
from .forms import FormAnexosIdentifica,FormAnexosFormula

from django.forms import ModelForm, ClearableFileInput
from .models import Anexo, TipoAnexo
from pedidos.models import Solicitud

from django.views.generic.edit import FormView

class Home(TemplateView):
    template_name = 'upload/home_upload.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload/upload.html', context)


def document_list(request):
    document = Document.objects.all()
    return render(request, 'upload/document_list.html', {
        'document': document
    })


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload_document.html', {
        'form': form
    })


def delete_document(request, pk):
    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('document_list')


class DocumentListView(ListView):
    model = Document
    template_name = 'upload/all_document_list.html'
    context_object_name = 'documents'


class UploadDocumentView(CreateView):
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('all_document_list')
    template_name = 'upload/upload_document.html'

""" class ListOneDocumentView(ListView):
    template_name = "upload/one_document_list.html"

    def get_queryset(self):
        pr = self.request.GET.get('pk')
        context = Document.objects.filter(id=pr)
        print(context)
        return context """

class ListOneDocumentView(View):

    def post(self, request, *args, **kwargs):
        document = Document.objects.filter(id=request.POST['id'])
        response = HttpResponse(post.archivo, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="%s"' % post.archivo
        return response        


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
 
    
""" def anexos(request):
     
    template_name = "upload/anexos.html"
    form_class = FormAnexos

    if request.method == 'POST':
       form = FormAnexos(request.POST, request.FILES)
       print(form)
       if form.is_valid():
          solicitud = Solicitud.objects.filter(user=self.request.user.id).latest('id')
          idanexo = request.POST['idanexo']
          #texto = request.POST['texto']
          archivo = request.FILES['archivo']
           
          insert = Anexo(idanexo=idanexo,idsolicitud=solicitud.id,archivo=archivo)
          insert.save()

          print('form no valid') 
          return HttpResponseRedirect(reverse('pedidos:pedidos'))
       else:
            messages.error(request, "Error al procesar el formulario")
    else:
         print('No Post') 
         return HttpResponseRedirect(reverse('pedidos:pedidos')) """


from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def AnexosIdentificacion(request):
    solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
    if Anexo.objects.filter(idsolicitud=solicitud.id).filter(idanexo=1).exists():
        Anexo.objects.filter(idsolicitud=solicitud.id).filter(idanexo=1).delete()
        
    if request.method == 'POST':
        form = FormAnexosIdentifica(request.POST, request.FILES)
        
        if form.is_valid():
            solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
            anexo = TipoAnexo.objects.get(id=1)
            archivo = request.FILES['archivo']
            insert = form.save(commit=False)
            insert.idanexo_id = anexo.id
            insert.idsolicitud_id=solicitud.id
            insert.achivo=archivo
            insert.save()
            return redirect('pedidos:finalizar_pedido')
    else:
        form = FormAnexosIdentifica()
    return render(request, 'upload/anexo_identificacion.html', {
        'form': form
    })

def AnexosFormula(request):
    solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
    if Anexo.objects.filter(idsolicitud=solicitud.id).filter(idanexo=2).exists():
        Anexo.objects.filter(idsolicitud=solicitud.id).filter(idanexo=2).delete()
    
    if request.method == 'POST':
      
        form = FormAnexosIdentifica(request.POST, request.FILES)
        
        if form.is_valid():
            # file is saved
            solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
            anexo = TipoAnexo.objects.get(id=2)
            archivo = request.FILES['archivo']
            insert = form.save(commit=False)
            insert.idanexo_id = anexo.id
            insert.idsolicitud_id=solicitud.id
            insert.achivo=archivo
            insert.save()
            return redirect('pedidos:finalizar_pedido')
    else:
        form = FormAnexosIdentifica()
    return render(request, 'upload/anexo_formula.html', {'form': form})    