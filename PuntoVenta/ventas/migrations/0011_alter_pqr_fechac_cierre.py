# Generated by Django 5.0.2 on 2024-03-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_alter_pqr_fechac_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='fechac_cierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]