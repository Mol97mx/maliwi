# Generated by Django 2.0.2 on 2018-07-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ['-creado'], 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(upload_to='proyectos'),
        ),
    ]