# Generated by Django 3.0.4 on 2020-03-27 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idciudad', models.CharField(blank=True, default='', max_length=3, null=True, verbose_name='Código Ciudad')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='CiudadDireccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idciudad', models.CharField(blank=True, default='', max_length=5, null=True, verbose_name='Código Ciudad')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Ciudad Direección',
                'verbose_name_plural': 'Ciudades Dirección',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iddepartamento', models.CharField(blank=True, default='', max_length=3, null=True, verbose_name='Código Departamento')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departementos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideps', models.CharField(blank=True, default='', max_length=3, null=True, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripción')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Eps',
                'verbose_name_plural': 'Eps',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idespecial', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Código Especialidad')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idgrupo', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Código Grupo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpais', models.CharField(blank=True, default='', max_length=3, null=True, verbose_name='Código País')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='PlanSalud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idplan', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Código Plan')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Plan Salud',
                'verbose_name_plural': 'Planes Salud',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha Solicitud')),
                ('direccion_envio', models.CharField(default='', max_length=100, verbose_name='Dirección de Envio')),
                ('telefono_envio', models.CharField(default='', max_length=35, verbose_name='Teléfono de Envio')),
                ('fecha_cirugia', models.DateField(auto_now_add=True, verbose_name='Fecha Solicitud')),
                ('valortotal', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Valor Total')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='TipoCirugia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcirugia', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Código Cirugía')),
                ('descripcion', models.CharField(max_length=35, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo Cirugía',
                'verbose_name_plural': 'Tipo Cirugía',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtipoidentifica', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Identificacion',
                'verbose_name_plural': 'Tipos de Identificacion',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='TipoInjerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtipoinjerto', models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='Código Tipo de Injerto')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio')),
                ('caracteristicas', models.CharField(blank=True, default='', max_length=2000, null=True, verbose_name='Características')),
                ('activo', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, default='static/core/img/placeholder.jpg', null=True, upload_to='fotos_injertos', verbose_name='Foto')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Especialidad', verbose_name='Especialidad')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Grupo', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Tipo de Injerto',
                'verbose_name_plural': 'Tipos de Injertos',
                'ordering': ['idtipoinjerto'],
            },
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Nro. Identificación')),
                ('nombre1', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='Primer Nombre')),
                ('nombre2', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='Segundo Nombre')),
                ('apel1', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='Primer Apellido')),
                ('apel2', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='Segundo Apellido')),
                ('razon_social', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Razon Social')),
                ('direccion', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, default='', max_length=35, null=True, verbose_name='Teléfono')),
                ('fecha_nacimiento', models.DateField(blank=True, default='', null=True, verbose_name='Fecha de Nacimiento')),
                ('edad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('nacionalidad', models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='Nacionalidad')),
                ('tipo_ter', models.CharField(blank=True, choices=[('paciente', 'Paciente'), ('hospital', 'Hospital'), ('medico', 'Medico'), ('pagador', 'Pagador')], default='', max_length=10, null=True, verbose_name='Tipo Tercero')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Edición')),
                ('ciudad', models.ForeignKey(blank=True, default='', max_length=5, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Ciudad', verbose_name='Ciudad Nacimiento')),
                ('ciudad_direccion', models.ForeignKey(blank=True, default='', max_length=5, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.CiudadDireccion', verbose_name='Ciudad Direcciòn')),
                ('departamento', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Departamento', verbose_name='Departamento Nacimiento')),
                ('eps', models.ForeignKey(blank=True, default='', max_length=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Eps', verbose_name='EPS')),
                ('especialidad', models.ForeignKey(blank=True, default='', max_length=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Especialidad', verbose_name='Ciudad Nacimiento')),
                ('pais', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pais', verbose_name='País Nacimiento')),
                ('plan_salud', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.PlanSalud', verbose_name='Plan Salud')),
                ('tipoidentificacion', models.ForeignKey(max_length=2, on_delete=django.db.models.deletion.CASCADE, to='pedidos.TipoIdentificacion', verbose_name='Tipo de Indetificación')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'Terceros',
                'ordering': ['apel1', 'apel2', 'nombre1', 'nombre2'],
            },
        ),
        migrations.CreateModel(
            name='SolicitudDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor')),
                ('valortotal', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor Total')),
                ('grupoinjerto', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pedidos.Grupo', verbose_name='Grupo del Injerto')),
                ('solicitud', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_detalle', to='pedidos.Solicitud')),
                ('tipoinjerto', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pedidos.TipoInjerto', verbose_name='Tipo de Injerto')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='hospital',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='pedidos.Tercero', verbose_name='Hospital'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='medico',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='pedidos.Tercero', verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='pedidos.Tercero', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='pagador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pagador', to='pedidos.Tercero', verbose_name='Pagador'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo_cirugia',
            field=models.ForeignKey(default='', max_length=4, on_delete=django.db.models.deletion.CASCADE, to='pedidos.TipoCirugia', verbose_name='Tipo Cirugía'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pais', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='pedidos.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pais', verbose_name='País'),
        ),
    ]