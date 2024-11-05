# Generated by Django 5.0.7 on 2024-10-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PurchaseEntry",
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
                ("party_name", models.CharField(max_length=255, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("item", models.CharField(max_length=255)),
                ("voucher_number", models.CharField(max_length=50)),
                ("voucher_date", models.DateField()),
                ("quantity", models.PositiveIntegerField()),
                ("rate", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "discount_percentage",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                (
                    "gst_percentage",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                (
                    "discount_amount",
                    models.DecimalField(
                        decimal_places=2, default=0, editable=False, max_digits=10
                    ),
                ),
                (
                    "taxable_amount",
                    models.DecimalField(
                        decimal_places=2, default=0, editable=False, max_digits=10
                    ),
                ),
                (
                    "gst_amount",
                    models.DecimalField(
                        decimal_places=2, default=0, editable=False, max_digits=10
                    ),
                ),
                (
                    "purchase_amount",
                    models.DecimalField(
                        decimal_places=2, default=0, editable=False, max_digits=10
                    ),
                ),
                (
                    "reference_voucher_number",
                    models.CharField(editable=False, max_length=20, unique=True),
                ),
            ],
        ),
    ]
