# Generated by Django 3.2.16 on 2024-07-29 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0004_plan_planclientevivienda_upgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='OrdenInstalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresApellidos', models.CharField(max_length=300)),
                ('cedula', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono1', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('observacion', models.CharField(blank=True, max_length=300, null=True)),
                ('direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.IntegerField(choices=[(1, 'No Instalado'), (2, 'Instalado'), (3, 'Eliminado')], default=1)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nacionalidadCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.nacionalidadcliente')),
                ('tipoCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.tipocliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='ordenInstalacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.ordeninstalacion'),
        ),
    ]
