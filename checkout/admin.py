from django.contrib import admin
from .models import Orders, OrderItem
from django import forms
# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    list_display = ['product', 'price', 'quantity']
    extra = 1


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['First_Name', 'Last_Name', 'Customer', 'is_paid']

    inlines = [
        OrderItemsInline
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'Note':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        if db_field.name == 'Address':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
