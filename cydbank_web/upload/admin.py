from django.contrib import admin

# Register your models here.

from upload.models import Document,TipoAnexo,Anexo

class DocumentAdmin(admin.ModelAdmin):
    list_display= ('title','author','pdf','cover')
    search_fields = ['title']
    list_per_page = 30

admin.site.register(Document, DocumentAdmin)

class TipoAnexoAdmin(admin.ModelAdmin):
    list_display= ('descripcion',)
    search_fields = ['decripcion']
    list_per_page = 30

admin.site.register(TipoAnexo, TipoAnexoAdmin)

class AnexoAdmin(admin.ModelAdmin):
    list_display= ('idanexo','idsolicitud','archivo',)
    search_fields = ['idsolicitud']
    list_per_page = 30

admin.site.register(Anexo, AnexoAdmin)