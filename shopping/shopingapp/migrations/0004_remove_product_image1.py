# Generated by Django 4.2.2 on 2023-08-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopingapp', '0003_product_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
    ]