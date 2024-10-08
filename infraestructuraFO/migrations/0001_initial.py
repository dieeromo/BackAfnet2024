# Generated by Django 3.2.16 on 2024-09-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0020_auto_20240818_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='CableFibra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRuta', models.CharField(max_length=300)),
                ('numeroBuffers', models.IntegerField()),
                ('numeroHilos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CajaNap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroNap', models.IntegerField()),
                ('nombreNap', models.CharField(blank=True, max_length=300, null=True)),
                ('splitter', models.IntegerField(blank=True, null=True)),
                ('splitter_adicional', models.IntegerField(blank=True, null=True)),
                ('puertos', models.IntegerField(blank=True, null=True)),
                ('puertosDanados', models.IntegerField(default=0)),
                ('potencia', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('coordenadas', models.CharField(blank=True, max_length=300, null=True)),
                ('verificado', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('barrio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.barrio')),
                ('comunidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='HiloFibra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hilo', models.IntegerField(choices=[(1, 'azul'), (2, 'tomate'), (3, 'verde')], default=1)),
                ('buffer', models.IntegerField(choices=[(1, 'azul'), (2, 'tomate'), (3, 'verde')], default=1)),
                ('cableFibra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.cablefibra')),
            ],
        ),
        migrations.CreateModel(
            name='Mufa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('splitter', models.IntegerField(blank=True, null=True)),
                ('splitter_adicional', models.IntegerField(blank=True, null=True)),
                ('potencia', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('coordenadas', models.CharField(blank=True, max_length=300, null=True)),
                ('verificado', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('barrio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.barrio')),
                ('comunidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='ODF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OLT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PuertoODF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puerto', models.IntegerField()),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('odf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.odf')),
            ],
        ),
        migrations.CreateModel(
            name='PuertoTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puerto', models.CharField(max_length=30)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoFibra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Trazo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conexion_splitter', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('verificado', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('caja_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.cajanap')),
                ('hilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.hilofibra')),
                ('mufa_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.mufa')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.puertoodf')),
            ],
        ),
        migrations.CreateModel(
            name='Trazo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conexion_splitter', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('verificado', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('caja_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.cajanap')),
                ('hilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.hilofibra')),
                ('mufa_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.mufa')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.trazo1')),
            ],
        ),
        migrations.CreateModel(
            name='TrazoPachcord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('verificado', models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)),
                ('lleg_puertoODF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.puertoodf')),
                ('sal_puertoTarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.puertotarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Trazo3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conexion_splitter', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('verificado', models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)),
                ('caja_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.cajanap')),
                ('hilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.hilofibra')),
                ('mufa_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.mufa')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.trazo2')),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaOLT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_instalacion', models.DateField(blank=True, null=True)),
                ('olt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.olt')),
            ],
        ),
        migrations.AddField(
            model_name='puertotarjeta',
            name='tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.tarjetaolt'),
        ),
        migrations.AddField(
            model_name='cajanap',
            name='mufa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.mufa'),
        ),
        migrations.AddField(
            model_name='cablefibra',
            name='tipoFibra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infraestructuraFO.tipofibra'),
        ),
    ]
