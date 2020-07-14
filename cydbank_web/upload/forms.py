from django import forms

from .models import Document

from django.forms import ModelForm, ClearableFileInput
from .models import Anexo
from pedidos.models import Solicitud

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'author', 'pdf', 'cover')


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
 
""" class FormAnexos(ModelForm):
    class Meta:
        model = Anexo
        fields = ('idanexo','archivo',)
        widgets = {
            'archivo': CustomClearableFileInput
        } """

""" class FormAnexos(forms.Form):

    archivo = forms.FileField()
     
    def __init__(self, *args, **kwargs):
        super(FormAnexos, self).__init__(*args, **kwargs)
         
    def handle_uploaded_file(self, f):
        with open('media/' + f.name, 'w') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    class Meta:
        model = Anexo
        fields = ('idanexo','archivo',)
        widgets = {
            'archivo': CustomClearableFileInput
        }       """

from django import forms
from .models import Anexo

""" class FormAnexos(forms.ModelForm):

    model = Anexo

    def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
       return super(FormAnexos, self).__init__(*args, **kwargs)


    def save(self, *args, **kwargs):
       kwargs['commit']=False
       obj = super(FormAnexos, self).save(*args, **kwargs)
       if self.request:
           obj.solicitud = Solicitud.objects.filter(user=self.request.user.id).latest('id')
           obj.solicitud_id = solicitud.id
           obj.idanexo_id = 1
       obj.save()
       return obj

    class Meta:
        fields = ('archivo','idanexo','idsolicitud')       """

class FormAnexosIdentifica(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
       return super(FormAnexosIdentifica, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
       kwargs['commit']=False
       obj = super(FormAnexosIdentifica, self).save(*args, **kwargs)
       if self.request:
           obj.solicitud = Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).latest('id')
           obj.solicitud_id = solicitud.id
           obj.idanexo_id = 1
       obj.save()
       return obj
    
    class Meta:
        model = Anexo
        fields = ('archivo','idanexo','idsolicitud')
        widgets = {'idanexo': forms.HiddenInput(),'idsolicitud': forms.HiddenInput()}
        

class FormAnexosFormula(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
       return super(FormAnexosFormula, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
       kwargs['commit']=False
       obj = super(FormAnexosFormula, self).save(*args, **kwargs)
       if self.request:
           obj.solicitud = Solicitud.objects.filter(user=self.request.user.id).filter(cerrada=False).latest('id')
           obj.solicitud_id = solicitud.id
           obj.idanexo_id = 2
       obj.save()
       return obj
    
    class Meta:
        model = Anexo
        fields = ('archivo',)                