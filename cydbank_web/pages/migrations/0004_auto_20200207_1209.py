# Generated by Django 3.0.3 on 2020-02-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_pageimage_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageimage',
            name='detalle',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Detalle Foto'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='posicion',
            field=models.CharField(blank=True, choices=[('antes', 'Antes'), ('despues', 'Después')], default='', max_length=10, null=True, verbose_name='Posición Foto'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='titulo',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Título Foto'),
        ),
    ]