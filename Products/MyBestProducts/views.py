
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

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
