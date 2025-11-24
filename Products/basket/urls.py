from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_view, name='basket'),  
    path('add/<int:product_id>/', views.add_to_basket, name='add_basket'),  
    path('delete/<int:product_id>/', views.delete_from_basket, name='delete_basket'), 
]
