# Generated by Django 3.2.16 on 2024-08-06 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_planclientevivienda_estado'),
        ('contabilidad', '0011_auto_20240805_0956'),
        ('inventario', '0006_equipo_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipoinstalado',
            name='condicion',
            field=models.IntegerField(blank=True, choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Dañado')], null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='contabilidad.facturaequipo'),
        ),
        migrations.AlterField(
            model_name='equipoinstalado',
            name='planClienteVivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipoInstalado', to='cliente.planclientevivienda'),
        ),
    ]
