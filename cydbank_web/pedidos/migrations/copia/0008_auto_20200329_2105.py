# Generated by Django 3.0.4 on 2020-03-30 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20200329_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tercero',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default='01/01/1900', null=True, verbose_name='Fecha de Nacimiento'),
        ),
    ]
