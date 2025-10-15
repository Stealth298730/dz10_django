from django.contrib.auth.forms import UserCreationForm
from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),label="Назва продукту")
    description = forms.CharField(max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}),label="Опис продукту")
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),label="Ціна продукту ")


    class Meta:
        model = Product              
        fields = ["name", "description", "price"]