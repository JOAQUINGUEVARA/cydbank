from django import forms
from .models import Solicitud,SolicitudDetalle,Tercero,TipoInjerto
#from django.forms.models import inlineformset_factory
#from crispy_forms.helper import FormHelper


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ['identificacion','tipoidentificacion','razon_social','ciudad_direccion','direccion','telefono','email']
        
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control','placeholder':'Nit'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control','placeholder':'Razòn Social'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }        

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ['identificacion','tipoidentificacion','nombre1','nombre2','apel1','apel2','especialidad','telefono','email']
        
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control','placeholder':'Identificacion'}),
            'nombre1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Nombre'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Nombre'}),
            'apel1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Apellido'}),
            'apel2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Apellido'}),
            #'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),

        }        

class PagadorForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ['identificacion','tipoidentificacion','nombre1','nombre2','apel1','apel2','razon_social','ciudad_direccion','direccion','telefono','email']
        
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control','placeholder':'Identificacion/Nit'}),
            'nombre1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Nombre'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Nombre'}),
            'apel1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Apellido'}),
            'apel2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Apellido'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control','placeholder':'razón Social'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ['identificacion','tipoidentificacion','nombre1','nombre2','apel1','apel2','ciudad','eps','plan_salud','fecha_nacimiento',]
        
        widgets = {
            'identificacion': forms.TextInput(attrs={'class':'form-control','placeholder':'identificacion'}),
            'nombre1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Nombre'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Nombre'}),
            'apel1': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Apellido'}),
            'apel2': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Apellido'}),
            #'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}),
            #'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono'}),
            'fecha_nacimiento': forms.DateInput(format='%d/%m/%Y'),
        }        


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['paciente','hospital','medico','pagador','id_recibe','nombre_recibe','ciudad_envio','direccion_envio','telefono_envio','tipo_cirugia','fecha_cirugia','valortotal']
        widgets = {
            'id_recibe': forms.TextInput(attrs={'class':'form-control','placeholder':'Identificación Recibe'}),
            'nombre_recibe': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Recibe'}),
            'direccion_envio': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}),
            'telefono_envio': forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono Envío'}),
            'fecha_cirugia': forms.DateInput(format='%d/%m/%Y'),
        }
        
        
class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = SolicitudDetalle
        exclude =['solicitud',]
        fields = ['tipoinjerto','cantidad','valor','valortotal']
        
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad válida")
        return cantidad

    def clean_valor_pedido(self):
        valor = self.cleaned_data['valor']
        if valor =='':
            raise forms.ValidationError("Debe ingresar un precio válido")
        return valor

class TipoInjertoForm(forms.ModelForm):
    class Meta:
        model = TipoInjerto
        fields = ['idtipoinjerto','descripcion','especialidad','valor','caracteristicas','activo','foto']
        
""" class TipoInjertoFilterFormHelper(crispy_forms.helper.FormHelper):
    form_method = 'GET'
    layout = Layout(
        'descripcion',
        'especialidad',
        Submit('submit', 'Apply Filter'),
    )
 """

class TerceroRangoFechaForm(forms.Form):
    
    class Meta:
        widgets = {
        'fecha1' : forms.TextInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Fecha Inicial'}),
        'fecha2' : forms.TextInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Fecha Final'}),}

class AnexosForm(forms.Form):
    image1 = forms.Field(label='Anexo Identificación', widget = forms.FileInput,required = True )
    image2 = forms.Field(label='Anexo Fórmula Médica ', widget = forms.FileInput,required = True )            