from django import forms

from products.models import Products


class ProductsCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name' , 'content' , 'price', 'img', 'category' ,]