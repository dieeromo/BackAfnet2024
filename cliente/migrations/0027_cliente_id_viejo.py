# Generated by Django 3.2.16 on 2024-09-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0026_planclientevivienda_estadogeneracionpagos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id_viejo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
