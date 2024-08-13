# Generated by Django 3.2.16 on 2024-07-29 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresApellidos', models.CharField(max_length=300)),
                ('cedula', models.CharField(max_length=30)),
                ('telefono1', models.CharField(max_length=30)),
                ('telefono2', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=300)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioCliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunidad', to='cliente.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='NacionalidadCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=300)),
                ('coordenadas', models.CharField(max_length=100)),
                ('barrio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='barrio', to='cliente.barrio')),
                ('comunidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunidad', to='cliente.comunidad')),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioVivienda', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteVivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo', models.IntegerField(choices=[(1, 'Propia'), (2, 'Arrendada'), (3, 'Otro')], default=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='cliente.cliente')),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioClienteVivienda', to=settings.AUTH_USER_MODEL)),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vivienda', to='cliente.vivienda')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='nacionalidadCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nacionalidadCliente', to='cliente.nacionalidadcliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipoCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipoCliente', to='cliente.tipocliente'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciudad', to='cliente.ciudad'),
        ),
    ]
