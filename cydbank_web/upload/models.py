from django.db import models
from pedidos.models import Solicitud

class Document(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='upload/pdfs/')
    cover = models.ImageField(upload_to='upload/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class TipoAnexo(models.Model):
    descripcion = models.CharField(max_length=30)
    
    def __str__(self):
        return self.descripcion

    class Admin:
        pass

class Anexo(models.Model):
    idanexo = models.ForeignKey(TipoAnexo,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Tipo Anexo')
    idsolicitud = models.ForeignKey(Solicitud,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Solicitud No.')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo No.'+str(self.idanexo)+' Solicitud No.'+str(self.idsolicitud)
    
    class Admin:
        pass

