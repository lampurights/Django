from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


from .cart import Cart
from products.models import Product
from .forms import AddToCartForm


def cart_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_quantity_update_form'] = AddToCartForm(initial={
            'product_quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {"cart": cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST)
    print(form)
    if form.is_valid():
        cleand_data = form.cleaned_data
        quantity = cleand_data['product_quantity']
        inplace = cleand_data['inplace']
        cart.add(product, quantity, inplace)

    return redirect('cart:cart_detail')


def delete_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    cart.clear(product)

    return redirect('cart:cart_detail')
