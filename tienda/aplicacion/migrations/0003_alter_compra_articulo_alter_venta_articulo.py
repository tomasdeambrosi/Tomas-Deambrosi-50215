# Generated by Django 5.0.2 on 2024-03-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_remove_articulo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='articulo',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='venta',
            name='articulo',
            field=models.CharField(max_length=60),
        ),
    ]
