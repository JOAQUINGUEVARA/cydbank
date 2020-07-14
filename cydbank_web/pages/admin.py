from django.contrib import admin
from pages.models import GrupoPage,PageImage,Page,Faq,ListaTecnica, GrupoTecnico

# Register your models here.
""" class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
 """
""" class PageImageAdmin(admin.ModelAdmin):
    list_display = ('page', 'image')
    
admin.site.register(PageImage, PageImageAdmin) """

class PageImageInline(admin.StackedInline):
    model = PageImage
    extra = 3

class PageAdmin(admin.ModelAdmin):
    
    inlines = [ PageImageInline ]

admin.site.register(Page, PageAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('nombre','grupo','order',)
    
admin.site.register(GrupoPage, PageAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display= ('title','content','order','created','updated')
    search_fields = ['title']
    list_per_page = 30

admin.site.register(Faq, FaqAdmin) 

class GrupoTecnicoAdmin(admin.ModelAdmin):
    list_display= ('descripcion','caracteristicas','order')
    search_fields = ['descripcion']
    list_per_page = 30

admin.site.register(GrupoTecnico, GrupoTecnicoAdmin)

class ListaTecnicaAdmin(admin.ModelAdmin):
    list_display= ('grupo','descripcion','proceso','cirugia','image','uso')
    search_fields = ['descripcion']
    list_per_page = 30

admin.site.register(ListaTecnica, ListaTecnicaAdmin)
