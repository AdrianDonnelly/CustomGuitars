from django.urls import path
from .views import SearchResultsListView

app_name='search_app'

urlpatterns = [
  path('search/', SearchResultsListView.as_view(), name='search_results'),
]