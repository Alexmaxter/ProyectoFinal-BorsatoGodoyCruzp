# Generated by Django 4.0.6 on 2022-07-26 23:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CuentaApp', '0002_rename_user_usuario_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuario',
            new_name='MasDatosUsuarios',
        ),
        migrations.RenameField(
            model_name='masdatosusuarios',
            old_name='usuario',
            new_name='user',
        ),
    ]