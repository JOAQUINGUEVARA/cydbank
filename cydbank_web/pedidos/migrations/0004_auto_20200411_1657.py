# Generated by Django 3.0.4 on 2020-04-11 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20200406_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicituddetalle',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2020, 4, 11), verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicituddetalle',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2020, 4, 11), verbose_name='Fecha de Edición'),
            preserve_default=False,
        ),
    ]
