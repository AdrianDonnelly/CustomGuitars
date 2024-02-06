from django.urls import path
from .import views
app_name = 'configurator'

urlpatterns = [
path('configurator/', views.configurator, name = 'configurator'),
]