# Generated by Django 3.0.4 on 2020-04-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0012_auto_20200401_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametrossolicitud',
            name='user',
            field=models.CharField(default='', max_length=35, verbose_name='Usuario'),
            preserve_default=False,
        ),
    ]
