# Generated by Django 5.0.7 on 2024-11-13 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("barcode", models.CharField(max_length=100)),
                ("item_name", models.CharField(max_length=255)),
                ("unit", models.PositiveIntegerField()),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("fullname", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("tax", models.DecimalField(decimal_places=2, max_digits=10)),
                ("discount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "grand_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("payment_method1", models.CharField(default="cash", max_length=100)),
                ("payment_method2", models.CharField(default="upi", max_length=100)),
                ("narration", models.TextField(blank=True, max_length=200, null=True)),
                (
                    "payment_method1_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "payment_method2_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="order_items", to="RetailSale.item"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="RetailSale.order",
            ),
        ),
    ]
