# Generated by Django 3.0.4 on 2020-04-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0014_auto_20200401_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Edición'),
        ),
    ]