from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from comments.forms import CommentForms
from .models import Product
from comments.models import Comments
from cart.forms import AddToCartForm
from cart.cart import Cart


# Create your views here.
class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'

    queryset = Product.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_one_to_cart_form'] = AddToCartForm(initial={
            'product_quantity': 1,
            'inplace': False,
        }
        )

        return context


class ProductsDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/products_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForms()
        context['product_form'] = AddToCartForm()
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comments
    form_class = CommentForms

    # def get_success_url(self):
    #     return reverse('products_detail', args=[int(self.kwargs['product_id'])])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        obj.product = get_object_or_404(Product, id=product_id)
        messages.success(self.request, _("comment added successfully"))
        return super().form_valid(form)




