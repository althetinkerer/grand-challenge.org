# Generated by Django 3.1.1 on 2020-11-24 11:25

import django.contrib.postgres.fields.citext
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anatomy", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="BodyStructure",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "structure",
                            django.contrib.postgres.fields.citext.CICharField(
                                max_length=16, unique=True
                            ),
                        ),
                        (
                            "region",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="anatomy.bodyregion",
                            ),
                        ),
                    ],
                    options={"ordering": ("region", "structure")},
                ),
            ],
            # Table already exists, see challenges/0031_move_bodystructure
            database_operations=[],
        ),
    ]
