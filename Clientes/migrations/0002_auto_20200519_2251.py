# Generated by Django 3.0.5 on 2020-05-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.CharField(blank=True, default='C/F', max_length=12, null=True, verbose_name='NIT'),
        ),
    ]
