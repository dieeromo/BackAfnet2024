# Generated by Django 3.2.16 on 2024-08-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0011_plan_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
