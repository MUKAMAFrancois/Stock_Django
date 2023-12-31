# Generated by Django 4.2.5 on 2023-10-17 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0010_alter_product_model_sold_by_purchase_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_model',
            name='purchased_on',
        ),
        migrations.RemoveField(
            model_name='product_model',
            name='qty_added',
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='purchase_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Sales_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.PositiveBigIntegerField()),
                ('sold_on', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.product_model')),
            ],
        ),
    ]
