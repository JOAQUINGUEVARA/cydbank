# Generated by Django 3.0.4 on 2020-03-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20200328_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='idespecial',
            field=models.CharField(blank=True, default='', max_length=3, null=True, verbose_name='Código Especialidad'),
        ),
        migrations.AlterField(
            model_name='tercero',
            name='especialidad',
            field=models.ForeignKey(blank=True, default='', max_length=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Especialidad', verbose_name='Especialidad'),
        ),
    ]
