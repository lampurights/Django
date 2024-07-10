from django.contrib import admin
from .models import Product
from comments.models import Comments


class CommentInline(admin.TabularInline):
    model = Comments
    fields = ['active', 'product_star', 'author', 'text']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [
        CommentInline,
    ]

