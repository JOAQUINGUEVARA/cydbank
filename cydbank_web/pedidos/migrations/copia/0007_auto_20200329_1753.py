# Generated by Django 3.0.4 on 2020-03-29 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_auto_20200328_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitud',
            options={'ordering': ['fecha'], 'verbose_name': 'Solicitud', 'verbose_name_plural': 'Solicitudes'},
        ),
        migrations.AlterModelOptions(
            name='solicituddetalle',
            options={'ordering': ['solicitud'], 'verbose_name': 'Detalle Solicitud', 'verbose_name_plural': 'Detalle Solicitudes'},
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='ciudad_envio',
            field=models.ForeignKey(default='', max_length=5, on_delete=django.db.models.deletion.CASCADE, to='pedidos.CiudadDireccion', verbose_name='Ciudad Envío'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='direccion_envio',
            field=models.CharField(max_length=100, verbose_name='Dirección de Envio'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_cirugia',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Cirugía'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hospital', to='pedidos.Tercero', verbose_name='Hospital'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Médico', to='pedidos.Tercero', verbose_name='Médico'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente', to='pedidos.Tercero', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='pagador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pagador', to='pedidos.Tercero', verbose_name='Pagador'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='telefono_envio',
            field=models.CharField(max_length=35, verbose_name='Teléfono de Envio'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipo_cirugia',
            field=models.ForeignKey(max_length=4, on_delete=django.db.models.deletion.CASCADE, to='pedidos.TipoCirugia', verbose_name='Tipo Cirugía'),
        ),
    ]
