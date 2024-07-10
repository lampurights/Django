from products.models import Product


class Cart:
    def __init__(self, request):
        self.request = request

        self.session = request.session

        cart = self.session.get("cart")

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1, inplace=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        elif inplace:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def clear(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        product_ids = self.cart.keys()
        return sum(self.cart[str(ids)]['quantity'] for ids in product_ids)

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(product.price * self.cart[str(product.id)]['quantity'] for product in products)

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

# session = {
#     '1': "asd",
#     'cart': {},
# }
#
# cart = {
#     '123':
#         {
#             'quantity': 1,
#             'product_obj': 0x55

#         },
#
#     '345':
#         {
#             'quantity': 2
#             'product_obj': 0x55
#             'inplace': True
#         }
#
# }
