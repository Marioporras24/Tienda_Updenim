# Generated by Django 5.0.2 on 2024-02-29 05:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_rename_idtipomovimiento_movimeinto_inventario_idtipo_movimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
