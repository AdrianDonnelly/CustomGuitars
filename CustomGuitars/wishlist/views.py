from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product, Wishlist
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from shop.forms import ProductReviewForm
from django.contrib.auth.decorators import login_required


def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    items = user_wishlist.objects.all()
    return render(request, 'products/wishlist.html', {'wishlist': wishlist})


def add_to_wishlist(request, item_id):
    item = Product.objects.get(pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.product.add()
    return redirect('wishlist')