# Generated by Django 4.2.5 on 2023-10-17 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0011_remove_product_model_purchased_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_model',
            name='qty_sold',
        ),
        migrations.RemoveField(
            model_name='product_model',
            name='sold_by',
        ),
        migrations.RemoveField(
            model_name='product_model',
            name='sold_on',
        ),
        migrations.RemoveField(
            model_name='product_model',
            name='time_of_order',
        ),
        migrations.CreateModel(
            name='Profitability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.product_model')),
                ('qty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.sales_history')),
            ],
        ),
    ]
