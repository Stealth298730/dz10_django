from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#from django.contrib.auth.models import User 
from .models import MySuperUser
from django import forms


class SignUp(UserCreationForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Логін"),
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Ім'я "),
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Прізвище "),
    email = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Електронна пошта "),
    phone_number = forms.CharField(max_length=15,required=False,widget=forms.TextInput(attrs={"class":"form-control"}),label = "Телефон секретної служби")
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Введіть пароль "),
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Повторіть пароль ")


    class Meta:
        model = MySuperUser
        fields = ("username","first_name","last_name", "email", "phone_number", "password1","password2",)


class Login(AuthenticationForm):
    username = forms.CharField(label="Логін",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"class":"form-control"}))