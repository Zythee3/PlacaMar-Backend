# Generated by Django 5.2.1 on 2025-07-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Placa",
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
                ("nome_placa", models.CharField(max_length=255)),
                ("subzona", models.CharField(max_length=50)),
                ("localidade", models.CharField(max_length=100)),
                ("embarcacoes", models.IntegerField()),
                ("usuarios", models.IntegerField()),
                ("cor", models.CharField(max_length=7)),
                ("descricao", models.TextField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
