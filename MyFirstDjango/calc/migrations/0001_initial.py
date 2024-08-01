# Generated by Django 5.0.7 on 2024-07-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=300, null=True)),
                ("age", models.CharField(max_length=300, null=True)),
                ("date", models.DateField(max_length=300, null=True)),
            ],
        ),
    ]
