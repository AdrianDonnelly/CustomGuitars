from django.contrib import admin
from .models import Category, Product,Guitar, ProductReview
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock', 'available', 'created', 'updated','featured','name', 'wood', 'neck', 'fretboard', 'frets', 'pickups', 'switches', 'mastervol', 'mastertone', 'trem', 'tuners', 'hardware', 'colour', 'scale']
    list_editable = ['price', 'stock', 'available','featured']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)


class GuitarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Guitar, GuitarAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating','date']
    
admin.site.register(ProductReview, ProductReviewAdmin)

