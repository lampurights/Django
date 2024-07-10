from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
from products.models import Product


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comments(models.Model):

    STAR_CHOICES = [
        ('1', _("Very Bad")),
        ('2', _("Bad")),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("comment author")
    )
    product_star = models.CharField(
        choices=STAR_CHOICES,
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_("? what is your star")
    )
    text = models.TextField(verbose_name=_("comment text"))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('products_detail', args=[self.product.id])
