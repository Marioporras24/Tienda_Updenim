# Generated by Django 5.0.2 on 2024-03-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_venta_precio_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='fechac_cierre',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]