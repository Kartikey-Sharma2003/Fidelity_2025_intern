from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=False)
    message=forms.CharField(max_length=200, widget=forms.Textarea, required=True)