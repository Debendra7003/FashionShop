# Generated by Django 5.0.7 on 2024-10-08 06:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("GarmentShopAPI", "0004_rename_category_code_category_catagory_code_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="Catagory",
        ),
    ]
