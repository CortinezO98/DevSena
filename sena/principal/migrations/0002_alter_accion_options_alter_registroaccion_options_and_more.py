# Generated by Django 5.0.2 on 2024-03-04 18:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("principal", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="accion",
            options={"verbose_name": "Acción", "verbose_name_plural": "Acciones"},
        ),
        migrations.AlterModelOptions(
            name="registroaccion",
            options={
                "verbose_name": "Registro de acción",
                "verbose_name_plural": "Registro de acciones",
            },
        ),
        migrations.CreateModel(
            name="Encuesta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dominioPersonaAtendio", models.IntegerField()),
                ("satisfaccionServicioRecibido", models.IntegerField()),
                ("recomendacionCanalAtencion", models.IntegerField()),
                ("solucionSolicitud", models.BooleanField()),
                ("ip", models.CharField(max_length=100)),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
