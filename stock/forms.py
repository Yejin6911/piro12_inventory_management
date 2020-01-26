from django import forms
from .models import Product, Account


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
