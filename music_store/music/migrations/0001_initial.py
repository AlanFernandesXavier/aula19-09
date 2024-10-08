# Generated by Django 5.1.1 on 2024-09-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Music",
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
                ("titulo", models.CharField(max_length=50)),
                ("artista", models.CharField(max_length=50)),
                ("album", models.CharField(max_length=50)),
                ("genero", models.CharField(max_length=50)),
                ("data", models.DateField()),
            ],
        ),
    ]
