# Generated by Django 3.2.16 on 2024-07-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaequipo',
            name='abono',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
