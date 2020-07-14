from django.contrib import admin
from import_export import fields,resources
from .models import Injertos
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class InjertoResource(resources.ModelResource):
    class Meta:
        model = Injertos
        skip_unchanged = True
        report_skipped = True
        fields = ('descripcion','proceso','uso_qx','foto')        
        exclude = ('id',)

@ admin.register (Injertos)
class Injerto(ImportExportModelAdmin):
    list_display= ('descripcion','proceso','uso_qx','foto')
    search_fields = ['descripcion']
    list_per_page = 50