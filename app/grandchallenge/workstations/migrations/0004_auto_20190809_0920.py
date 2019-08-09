# Generated by Django 2.2.4 on 2019-08-09 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("workstations", "0003_group_data_migration")]

    operations = [
        migrations.AlterField(
            model_name="workstation",
            name="editors_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="editors_of_workstation",
                to="auth.Group",
            ),
        ),
        migrations.AlterField(
            model_name="workstation",
            name="users_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_of_workstation",
                to="auth.Group",
            ),
        ),
    ]
