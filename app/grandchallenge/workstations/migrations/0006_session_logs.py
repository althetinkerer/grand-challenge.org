# Generated by Django 2.2.8 on 2019-12-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workstations", "0005_auto_20191015_1005"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="logs",
            field=models.TextField(blank=True, editable=False),
        ),
    ]
