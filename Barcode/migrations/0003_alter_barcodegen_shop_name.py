# Generated by Django 5.0.6 on 2024-11-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barcode', '0002_barcodegen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcodegen',
            name='shop_name',
            field=models.CharField(max_length=25),
        ),
    ]