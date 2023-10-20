# Generated by Django 4.2.5 on 2023-10-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0007_alter_product_model_category_and_more'),
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
            field=models.CharField(blank=True, max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='time_of_order',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Issue_Product',
        ),
    ]