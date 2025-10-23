
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.views.decorators.http import require_GET,require_POST
from django.views.generic import ListView,FormView

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "product_create.html", {"form": form, "title": "Додати"})


def product_delete(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Product.objects.filter(name=name).delete()
        return redirect("product_list")
    return render(request, "product_delete.html")


def product_list(request: HttpRequest):
    products = Product.objects.all().order_by("id")       
    paginator = Paginator(products, 2)                    
    page_number = request.GET.get("page")                 
    page_obj = paginator.get_page(page_number)

    return render(request, "product_list.html", {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "title": "Продукти"
    })


def index(request):
    return render(request=request,template_name="index.html")