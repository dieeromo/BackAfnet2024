# Generated by Django 3.2.16 on 2024-08-15 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0017_auto_20240814_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagosplanclientevivienda',
            name='fecha_pago',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='upgrade',
            name='planClienteVivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upgrades', to='cliente.planclientevivienda'),
        ),
    ]
