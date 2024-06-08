# Generated by Django 5.0.3 on 2024-05-03 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("players", "0005_region_alter_chessplayers_region"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournament",
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
                ("title", models.CharField(max_length=50, verbose_name="")),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("open", "Open"), ("man", "Man"), ("woman", "Woman")],
                        default="open",
                        max_length=5,
                    ),
                ),
                ("has_age_limit", models.BooleanField(default=False)),
                ("min_age", models.PositiveIntegerField(blank=True, null=True)),
                ("max_age", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "players",
                    models.ManyToManyField(
                        related_name="tournaments", to="players.chessplayers"
                    ),
                ),
            ],
        ),
    ]
