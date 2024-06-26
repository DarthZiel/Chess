# Generated by Django 5.0.3 on 2024-03-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_remove_user_is_admin_user_groups_user_is_superuser_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChessPlayers",
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
                ("fide_id", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name_fide", models.CharField(max_length=20)),
                ("first_name_fide", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=2)),
                (
                    "gender",
                    models.CharField(
                        choices=[("FEMALE", "FEMALE"), ("MALE", "MALE")], max_length=14
                    ),
                ),
                ("federation", models.CharField(max_length=3)),
                ("rating_classical", models.CharField(max_length=4)),
                ("rating_rapid", models.CharField(max_length=4)),
                ("rating_blitz", models.CharField(max_length=4)),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("Абайская область", "Абайская область"),
                            ("Акмолинская область", "Акмолинская область"),
                            ("Актюбинская область", "Актюбинская область"),
                            ("Алматинская область", "Алматинская область"),
                            ("Атырауская область", "Атырауская область"),
                            (
                                "Восточно-Казахстанская область",
                                "Восточно-Казахстанская область",
                            ),
                            ("Жамбылская область", "Жамбылская область"),
                            ("Жетысуская область", "Жетысуская область"),
                            (
                                "Западно-Казахстанская область",
                                "Западно-Казахстанская область",
                            ),
                            ("Карагандинская область", "Карагандинская область"),
                            ("Костанайская область", "Костанайская область"),
                            ("Кызылординская область", "Кызылординская область"),
                            ("Мангистауская область", "Мангистауская область"),
                            ("Павлодарская область", "Павлодарская область"),
                            (
                                "Северо-Казахстанская область",
                                "Северо-Казахстанская область",
                            ),
                            ("Туркестанская область", "Туркестанская область"),
                            ("Улытауская область", "Улытауская область"),
                            ("Астана", "Астана"),
                            ("Алматы", "Алматы"),
                            ("Шымкент", "Шымкент"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
    ]
