from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpRequest,HttpResponseForbidden

from .models import MySuperUser
from .forms import SignUp,Login
# Create your views here.


def sign_up(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")
    print("POST?=",request.POST)


    form = SignUp(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.add_message(request=request,level=messages.SUCCESS,message="Вітаю з реєстрацією")
        return redirect("index")
    
    return render(request,"sign_up.html",{"form":form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = Login(data=request.POST or None)
    if request.method=="POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        if user:
            login(request=request,user=user)
            messages.add_message(request=request,level=messages.SUCCESS,message="Вітаю з входом")
            return redirect("index")
        else:
            messages.add_message(request=request,level=messages.ERROR,message="Спробуйте ще раз")

    return render(request=request,template_name="sign_in.html",context=dict(form=form))
    
@login_required(login_url="/sign_in/")
def index(request):
    print(request.COOKIES)
    return render(request=request,template_name="index.html")


@login_required(login_url="/sign_in/")
def logout_func(request):
        logout(request)
        messages.success(request,"Ви успішно ввійшли")
        return redirect("sign_in")