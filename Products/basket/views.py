from django.shortcuts import redirect, get_object_or_404, render
from .models import Basket, Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket_item, created = Basket.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'count': 1}
    )
    if not created:
        basket_item.count += 1
        basket_item.save()
    return redirect('basket')

@login_required
def basket_view(request):
    items = Basket.objects.filter(user=request.user)
    return render(request, "basket.html", {"items": items})

@login_required
def delete_from_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Basket.objects.filter(user=request.user, product=product).delete()
    return redirect('basket')
