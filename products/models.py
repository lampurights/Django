from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='image_filed', blank=True, upload_to='product/product_cover/')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('products_detail', args=[self.id])

    def __str__(self):
        return f"{self.title}"

