# Generated by Django 4.0.6 on 2022-08-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_masdatosusuarios_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuarios',
            name='avatar',
            field=models.ImageField(blank=True, default='https://i.imgur.com/Pbm2fdP.png', null=True, upload_to='avatares'),
        ),
    ]
