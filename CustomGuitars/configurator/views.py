from django.shortcuts import render
from shop.models import Product

def configurator(request):
    return render(request, 'configurator.html')


def showroom(request):
    showroom = []
    showroom_products = Product.objects.filter(showroom=True, available=True)

    return render(request,'showroom.html',{'showroom':showroom_products,})