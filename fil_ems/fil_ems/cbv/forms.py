from . import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_id', 'prod_name', 'quantity', 'price']
        widgets = {
            'prod_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'prod_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
