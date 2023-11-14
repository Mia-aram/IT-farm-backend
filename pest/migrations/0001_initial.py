# Generated by Django 4.2.6 on 2023-11-13 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("farms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pest",
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
                ("problum", models.TextField(null=True)),
                ("photo", models.CharField(max_length=100, null=True)),
                ("solution", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "farm_id",
                    models.ForeignKey(
                        db_column="farm_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="farms.farms",
                    ),
                ),
            ],
        ),
    ]
