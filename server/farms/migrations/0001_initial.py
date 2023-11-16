# Generated by Django 4.2.7 on 2023-11-16 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Farms",
            fields=[
                ("farm_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("area", models.IntegerField(default=0)),
                ("mail_number", models.IntegerField(default=0)),
                ("address", models.CharField(max_length=100)),
                ("address_detail", models.CharField(max_length=100)),
                ("center", models.CharField(max_length=100)),
                ("method", models.CharField(max_length=100)),
                ("quantity", models.IntegerField(default=0)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
