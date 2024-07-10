from django.db import models
from django.conf import settings

from products.models import Product

# Create your models here.


class Orders(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    Phone_Number = models.CharField(max_length=11)
    Note = models.CharField(max_length=500, blank=True)
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'order'

    def __str__(self):
        return f"order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order.id}   {self.product} {self.price} '

