# Generated by Django 3.2.16 on 2024-09-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0028_auto_20240917_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordeninstalacion',
            name='fecha_instalacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
