# Generated by Django 5.0.2 on 2024-04-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/image', verbose_name='image_filed'),
        ),
    ]