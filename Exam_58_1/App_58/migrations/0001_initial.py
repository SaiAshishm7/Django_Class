# Generated by Django 5.0.7 on 2024-10-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMIRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('bmi', models.FloatField()),
                ('date_calculated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
