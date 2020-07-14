from django.db import models

# Create your models here.

class Injertos(models.Model):
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    proceso = models.CharField(max_length=40,blank=True,default='',verbose_name='Características')
    uso_qx = models.CharField(max_length=2000,blank=True,default='',verbose_name='Características')
    foto = models.ImageField(verbose_name="Foto", upload_to="fotos_injertos",null=True,blank=True,default='static/img/placeholder.jpg')
    
    class Meta:
        ordering=["descripcion"]
        verbose_name='Injerto'
        verbose_name_plural='Injertos'

    def __str__(self):
        return self.descripcion	 

    def get_foto(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return '/fotos_injertos/'
