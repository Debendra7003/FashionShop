# Generated by Django 5.0.7 on 2024-10-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GarmentShopAPI", "0019_remove_item_category_item_category_item"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="design",
            name="associated_items",
        ),
        migrations.AddField(
            model_name="design",
            name="associated_items",
            field=models.JSONField(default=list),
        ),
    ]