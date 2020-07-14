from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    empresa = forms.CharField(required=True)
    cargo = forms.CharField(required=True)
    ciudad = forms.CharField(required=True)
    pais = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True)
    #subject = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

    