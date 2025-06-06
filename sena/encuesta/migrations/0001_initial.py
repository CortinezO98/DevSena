# Generated by Django 5.0.2 on 2024-04-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("dominioPersonaAtendio", models.IntegerField(blank=True, null=True)),
                (
                    "satisfaccionServicioRecibido",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "recomendacionCanalAtencion",
                    models.IntegerField(blank=True, null=True),
                ),
                ("solucionSolicitud", models.BooleanField(blank=True, null=True)),
                ("idInteraccion", models.CharField(max_length=150)),
                ("nombreAgente", models.CharField(max_length=150)),
                ("token", models.CharField(max_length=50)),
                ("fechaExpiracionLink", models.DateTimeField()),
            ],
        ),
    ]
