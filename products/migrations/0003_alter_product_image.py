# Generated by Django 5.0.2 on 2024-04-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='image_filed'),
        ),
    ]
