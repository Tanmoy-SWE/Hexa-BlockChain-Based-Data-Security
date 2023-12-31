# Generated by Django 4.2.3 on 2023-07-18 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blockchain",
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
                ("data", models.CharField(max_length=255)),
                ("hash", models.CharField(max_length=64)),
                ("prev_hash", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Block",
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
                ("data", models.CharField(max_length=255)),
                ("hash", models.CharField(max_length=64)),
                ("prev_hash", models.CharField(max_length=64)),
                (
                    "blockchain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blocks",
                        to="blockchain.blockchain",
                    ),
                ),
            ],
        ),
    ]
