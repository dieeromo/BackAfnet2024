# Generated by Django 3.2.16 on 2024-09-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0022_ordencobro_dias_consumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='planclientevivienda',
            name='fecha_upgrade',
            field=models.DateField(blank=True, null=True),
        ),
    ]
