# Generated by Django 4.2.5 on 2023-10-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='person.jfif', upload_to='Profile_Images'),
        ),
    ]