from django.contrib import admin
from .models import Category, Product, Wishlist
from django.contrib import admin

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['product', 'available']
    
admin.site.register(Wishlist, WishlistAdmin)