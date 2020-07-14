from django.db import models
from ckeditor.fields import RichTextField

class GrupoPage(models.Model):
    nombre = models.CharField(verbose_name='Grupo Páginas', max_length=100)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    class Meta:
        verbose_name = "Grupo Página"
        verbose_name_plural = "Grupos Páginas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Page(models.Model):
    grupo = models.ForeignKey(GrupoPage,on_delete=models.CASCADE,related_name='grupo',null=True,blank=True,default='')
    title = models.CharField(verbose_name="Título Página", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    #foto = models.ImageField(verbose_name="Foto", upload_to="pages/images",null=True,blank=True,default='static/images/placeholder.png')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    

class PageImage(models.Model):
    POSICION_FOTO = (
        ('antes', 'Antes'),
		('despues', 'Después'),
    )
    page = models.ForeignKey(Page,on_delete=models.CASCADE, related_name='images')
    titulo = models.CharField(verbose_name="Título Foto", max_length=200,null=True,blank=True,default='')
    detalle = models.CharField(verbose_name="Detalle Foto", max_length=200,null=True,blank=True,default='')
    posicion = models.CharField(max_length=10,choices=POSICION_FOTO,verbose_name='Posición Foto',null=True,blank=True,default='')
    image = models.ImageField(upload_to="img/",null=True,blank=True,default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/img'

    """ def __str__(self):
        return self.image """

    def __unicode__(self,):
        return str(self.image)

class Faq(models.Model):
    title = models.CharField(verbose_name="Título Página", max_length=600)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "faq"
        verbose_name_plural = "faqs"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class GrupoTecnico(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=50)
    caracteristicas = RichTextField(verbose_name="Contenido",null=True,blank=True,default='')
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    class Meta:
        verbose_name = "Grupo Técnico"
        verbose_name_plural = "Grupos Técnicos"
        ordering = ['order', 'descripcion']

    def __str__(self):
        return self.descripcion

class ListaTecnica(models.Model):
    grupo = models.ForeignKey(GrupoTecnico,on_delete=models.CASCADE, related_name='grupo_tecnico')
    descripcion = models.CharField(verbose_name="Descripción", max_length=60,null=True,blank=True,default='')
    proceso = models.CharField(verbose_name="Proceso", max_length=60,null=True,blank=True,default='')
    cirugia = models.CharField(verbose_name="Cirugia", max_length=600,null=True,blank=True,default='')
    uso = models.PositiveIntegerField(default=1,verbose_name='Uso')
    image = models.ImageField(upload_to="img/",null=True,blank=True,default='')

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        """ else:
            return 'placeholder.png' """

    def __str__(self):
        return self.descripcion
    