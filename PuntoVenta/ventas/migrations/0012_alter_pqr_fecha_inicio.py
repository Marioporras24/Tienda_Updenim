# Generated by Django 5.0.2 on 2024-03-05 20:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_alter_pqr_fechac_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='fecha_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
