from django import forms


class AddToCartForm(forms.Form):
    choices = [(i, str(i)) for i in range(1, 31)]
    product_quantity = forms.TypedChoiceField(choices=choices, coerce=int)
    inplace = forms.BooleanField(widget=forms.HiddenInput(), required=False)
