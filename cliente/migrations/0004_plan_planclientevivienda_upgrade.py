# Generated by Django 3.2.16 on 2024-07-29 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0003_auto_20240729_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='PlanClienteVivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField()),
                ('fecha_pago', models.DateField()),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (2, 'Suspendido'), (3, 'Eliminado'), (4, 'CambioPlan')], default=1)),
                ('clienteVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.clientevivienda')),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('planClienteVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.planclientevivienda')),
                ('plan_upgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.plan')),
            ],
        ),
    ]
