# Generated by Django 3.2.16 on 2024-09-13 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ap_nodos',
            name='router',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mikrotik.router'),
        ),
    ]
