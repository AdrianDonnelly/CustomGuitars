from django.contrib import admin
from .models import Category, Product, Bestseller,Guitar, ProductReview
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)


class GuitarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Guitar, GuitarAdmin)

class BestsellerAdmin(admin.ModelAdmin):
    list_display = ['product']

admin.site.register(Bestseller, BestsellerAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating','date']
    
admin.site.register(ProductReview, ProductReviewAdmin)

