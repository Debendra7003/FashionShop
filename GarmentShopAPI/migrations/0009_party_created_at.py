# Generated by Django 5.0.7 on 2024-10-09 06:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GarmentShopAPI", "0008_party"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
