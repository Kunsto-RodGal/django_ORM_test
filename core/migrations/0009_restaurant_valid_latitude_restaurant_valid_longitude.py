# Generated by Django 5.1.1 on 2025-03-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_rating_rating_value_valid"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="restaurant",
            constraint=models.CheckConstraint(
                condition=models.Q(("latitude__gte", -90), ("latitude__lte", 90)),
                name="valid_latitude",
                violation_error_message="Invalid Latitude",
            ),
        ),
        migrations.AddConstraint(
            model_name="restaurant",
            constraint=models.CheckConstraint(
                condition=models.Q(("longitude__gte", -90), ("longitude__lte", 90)),
                name="valid_longitude",
                violation_error_message="Invalid longitude",
            ),
        ),
    ]
