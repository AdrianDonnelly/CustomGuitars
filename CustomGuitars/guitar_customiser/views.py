from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def customiser(request):
    customiser = customiser.objects.select_related('product').filter(product__available=True)
    products = Product.objects.filter(id__in=bestsellers.values_list('product_id', flat=True))
    return render(request, 'shop/bestsellers.html', {'bestsellers': bestsellers, 'prods': products})