# Generated by Django 4.0.6 on 2022-07-27 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CuentaApp', '0003_rename_usuario_masdatosusuarios_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masdatosusuarios',
            old_name='user',
            new_name='usuario',
        ),
    ]