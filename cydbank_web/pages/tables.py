from .models import ListaTecnica
from django.utils.html import format_html
import django_tables2

class ImageColumn(django_tables2.Column):
    def render(self, value):
        return format_html('<img src="{{ table.get_image }}" />', value)

class VitrinaTable(django_tables2.Table):
    img = ImageColumn()
    class Meta:
        model = ListaTecnica
        template_name = "django_tables2/bootstrap.html"
        fields = ("descripcion", )