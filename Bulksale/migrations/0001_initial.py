# Generated by Django 5.0.6 on 2024-11-22 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoicenumber', models.CharField(editable=False, max_length=5, unique=True)),
                ('partyname', models.CharField(max_length=255)),
                ('mobilenumber', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('gstnumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ItemInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcodenumber', models.CharField(max_length=255)),
                ('itemname', models.CharField(max_length=255)),
                ('unit', models.PositiveIntegerField()),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Bulksale.partyinformation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAndNarration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method1', models.CharField(max_length=255)),
                ('payment_method2', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_amount1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_amount2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('party', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_narration', to='Bulksale.partyinformation')),
            ],
        ),
        migrations.CreateModel(
            name='PricingAndTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('party', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_tax', to='Bulksale.partyinformation')),
            ],
        ),
    ]
