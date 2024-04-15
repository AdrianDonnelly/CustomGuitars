from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('',include('shop.urls')),
    path('',include('configurator.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('search/',include('search.urls')),
    path('vouchers/', include('vouchers.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
