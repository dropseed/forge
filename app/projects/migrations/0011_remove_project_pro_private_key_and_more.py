# Generated by Django 4.0.5 on 2022-06-23 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_alter_project_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="pro_private_key",
        ),
        migrations.RemoveField(
            model_name="project",
            name="pro_public_key",
        ),
    ]
