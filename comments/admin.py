from django.contrib import admin
from .models import Comments
# Register your models here.


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'active', 'product_star', 'author']
