# Generated by Django 5.0.2 on 2024-03-18 18:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("principal", "0003_registrodatosuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registrodatosuser",
            name="ubicacion_dispositivo",
        ),
    ]
