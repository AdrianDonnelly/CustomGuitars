from django.urls import path
from .import views
app_name = 'guitar_customiser'


path('customiser/', views.customiser, name = 'customiser'),