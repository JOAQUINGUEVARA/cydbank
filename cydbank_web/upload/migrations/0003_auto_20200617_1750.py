# Generated by Django 3.0.4 on 2020-06-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_anexo_tipoanexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='upload/anexos'),
        ),
    ]
