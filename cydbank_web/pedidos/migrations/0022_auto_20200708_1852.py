# Generated by Django 3.0.4 on 2020-07-08 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0021_auto_20200708_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='ciudad_envio',
            field=models.ForeignKey(default='1112', on_delete=django.db.models.deletion.CASCADE, to='pedidos.CiudadDireccion', verbose_name='Ciudad Envío'),
        ),
    ]
