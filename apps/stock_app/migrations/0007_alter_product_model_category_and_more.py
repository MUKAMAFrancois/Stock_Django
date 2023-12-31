# Generated by Django 4.2.5 on 2023-10-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0006_alter_product_model_sold_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='category',
            field=models.CharField(blank=True, choices=[('laptops', 'Laptops'), ('desktops', 'Desktops'), ('phones', 'Phones'), ('accessories', 'Accessories')], default='laptops', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product_model',
            name='product_name',
            field=models.CharField(blank=True, max_length=230, null=True),
        ),
    ]
