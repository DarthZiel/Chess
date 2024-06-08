# Generated by Django 5.0.3 on 2024-05-03 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0005_region_alter_chessplayers_region"),
        ("tournament", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tournament",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="players.region",
            ),
        ),
    ]
