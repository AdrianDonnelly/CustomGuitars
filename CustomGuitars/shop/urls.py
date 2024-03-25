from django.urls import path,include
from .import views
app_name = 'shop'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('featured/<str:category>/', views.featured, name='featured_category'),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>', views.product_detail, name = 'product_detail'),
    path('guitars/', views.guitars, name = 'guitars'),
    path('compare/', views.compare_detail, name = 'compare_detail'),
    path('add/<uuid:product_id>/', views.add_compare, name='add_compare'),
    path('remove/<uuid:product_id>/',views.compare_remove, name='compare_remove'),

    
]