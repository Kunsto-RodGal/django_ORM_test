# Generated by Django 5.1.1 on 2025-03-12 15:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_restaurant_valid_latitude_restaurant_valid_longitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="name",
            field=models.CharField(
                max_length=100,
                unique=True,
                validators=[core.models.validate_restaurant_name_begins_with_a],
            ),
        ),
    ]
