from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
  path('thanks/<int:order_id>/', views.thanks, name='thanks'),
  path('generate_order_pdf/<int:order_id>/', views.generate_order_pdf, name='generate_order_pdf'),
]