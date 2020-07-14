from django import forms

from pedidos.models import Solicitud,Paciente,Solicitante
from django.contrib.auth.models import User
#from .models import UserProfile
#from django.forms.models import inlineformset_factory


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PacienteForm(BaseForm, forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'fecha'}))

    class Meta:
        model = Paciente
        fields = ['identificacion','tipoidentificacion','nombre','direccion','pais','departamento','ciudad','nacionalidad','telefono','plan_salud','eps','fecha_nacimiento']
        
class SolicitanteForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['identificacion','tipoidentificacion','nombre','email','especialidad','direccion','telefono','pais','departamento','ciudad']
      
class SolicitudCreateForm(BaseForm, forms.ModelForm):
    #fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'fecha'}))

    class Meta:
        model = Solicitud
        fields = ['solicitante','paciente','direccion_envio','telefono_envio' ]

class SolicitudEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['solicitante','paciente','direccion_envio','telefono_envio' ]


""" class UserForm(BaseForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('identificacion','tipoidentificacion','nombre','email','especialidad','direccion','telefono','pais','departamento','ciudad')) """