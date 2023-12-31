# Generated by Django 4.2.5 on 2023-10-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_record_delete_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_ordered', models.PositiveBigIntegerField()),
                ('time_of_order', models.DateTimeField(auto_now_add=True)),
                ('sold_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_on', models.DateField(auto_created=True, null=True)),
                ('product_name', models.CharField(max_length=230)),
                ('items_instock', models.PositiveBigIntegerField(default=1)),
                ('category', models.CharField(choices=[('laptops', 'Laptops'), ('desktops', 'Desktops'), ('phones', 'Phones'), ('accessories', 'Accessories')], default='laptops', max_length=100)),
                ('unit_price', models.FloatField()),
                ('mgf_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('sold_on', models.DateField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('description', models.TextField(blank=True, default='Nice Product', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AddField(
            model_name='issue_product',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.product_model'),
        ),
    ]
