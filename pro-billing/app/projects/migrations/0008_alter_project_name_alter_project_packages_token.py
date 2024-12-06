# Generated by Django 4.0.5 on 2022-06-22 20:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_project_packages_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="packages_token",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
