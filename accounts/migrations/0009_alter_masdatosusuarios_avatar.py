# Generated by Django 4.0.6 on 2022-08-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_masdatosusuarios_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuarios',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
