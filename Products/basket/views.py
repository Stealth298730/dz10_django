from django.shortcuts import redirect, get_object_or_404, render
from .models import Basket, Product
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

def clear_user_basket_cache(user_id):
    cache_key = f'basket_user_{user_id}'
    cache.delete(cache_key)

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
    

    clear_user_basket_cache(request.user.id)

    return redirect('basket')

@login_required
def basket_view(request):
    items = Basket.objects.filter(user=request.user)
    return render(request, "basket.html", {"items": items})

@login_required
def delete_from_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Basket.objects.filter(user=request.user, product=product).delete()
    clear_user_basket_cache(request.user.id)
    return redirect('basket')
