# Generated by Django 4.0.6 on 2022-07-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcercaDeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(upload_to='empleados'),
        ),
    ]