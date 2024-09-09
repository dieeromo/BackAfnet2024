# Generated by Django 3.2.16 on 2024-09-08 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructuraFO', '0002_auto_20240906_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajanap',
            name='mufa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cajasNap', to='infraestructuraFO.mufa'),
        ),
        migrations.AlterField(
            model_name='mufa',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
