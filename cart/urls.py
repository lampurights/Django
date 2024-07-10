from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
   path('', views.cart_view, name='cart_detail'),
   path('add/<int:product_id>/', views.add_to_cart_view, name='cart_add'),
   path('delete/<int:product_id>/', views.delete_from_cart_view, name='cart_delete'),
]
