from django import forms
from crud_app .models import Orders
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=False)
    message= forms.CharField(max_length=200)

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'