from django import forms
from .models import Comments


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'product_star']
