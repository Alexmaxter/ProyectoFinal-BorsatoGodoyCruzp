# Generated by Django 4.0.6 on 2022-07-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CuentaApp', '0006_rename_username_masdatosusuarios_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='masdatosusuarios',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]