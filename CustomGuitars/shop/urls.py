from django.urls import path,include
from .import views
app_name = 'shop'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('featured/<str:category>/', views.featured, name='featured_category'),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>', views.product_detail, name = 'product_detail'),
    path('guitars/', views.guitars, name = 'guitars'),
    path('compare/', views.compare, name = 'compare'),
    path('compare/<str:category>/', views.compare, name='compare_products'),
    
]