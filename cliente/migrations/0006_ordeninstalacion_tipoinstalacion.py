# Generated by Django 3.2.16 on 2024-07-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20240729_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordeninstalacion',
            name='tipoInstalacion',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'Cambio operadora')], default=1),
        ),
    ]
