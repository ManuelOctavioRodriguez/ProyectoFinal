# Generated by Django 4.2.1 on 2023-05-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
    ]
