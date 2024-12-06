# Generated by Django 4.0.5 on 2022-06-21 19:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_project_pro_private_key_project_pro_public_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="packages_token",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
