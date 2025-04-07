# Generated by Django 5.1.1 on 2025-03-13 08:48

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_sale_profit"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="suggested_tip",
            field=models.GeneratedField(
                db_persist=True,
                expression=models.Case(
                    models.When(
                        income__gte=10,
                        then=django.db.models.expressions.CombinedExpression(
                            models.F("income"), "*", models.Value(0.2)
                        ),
                    ),
                    default=models.Value(0),
                    output_field=models.DecimalField(decimal_places=2, max_digits=8),
                ),
                output_field=models.DecimalField(decimal_places=2, max_digits=8),
            ),
        ),
    ]
