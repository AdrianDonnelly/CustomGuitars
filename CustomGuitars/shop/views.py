from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Bestseller
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def index(request):
    return render(request, 'home.html')
