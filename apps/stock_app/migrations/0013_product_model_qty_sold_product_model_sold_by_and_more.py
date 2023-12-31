# Generated by Django 4.2.5 on 2023-10-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0012_remove_product_model_qty_sold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='qty_sold',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='sold_by',
            field=models.CharField(blank=True, help_text='Your Names', max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='sold_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='time_of_order',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
