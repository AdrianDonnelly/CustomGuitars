from django.urls import path
from .views import SignUpView ,AccountView,ProfileUpdateView,OrderView
from .import views

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('accounts/account/<int:pk>/',AccountView.as_view(),name='account'),
    path('accounts/account_edit/<int:pk>/',ProfileUpdateView.as_view(),name='account_edit'),
    path('orders/',views.OrderView,name='orders'),
]
