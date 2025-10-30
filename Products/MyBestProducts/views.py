from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from .models import Product
from .forms import ProductForm



def index(request):
    main_products = Product.objects.filter(is_main=True)
    top_products = Product.objects.filter(is_top=True)

    return render(request, "index.html", {
        "main_products": main_products,
        "top_products": top_products
    })


def product_list(request):
    products = Product.objects.all().order_by("id")
    paginator = Paginator(products, 2)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "product_list.html", {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "title": "Продукти"
    })


@permission_required('MyBestProducts.product_create', raise_exception=True)  
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})


@permission_required('shop.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "product_delete.html", {"product": product})
