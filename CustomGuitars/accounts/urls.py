from django.urls import path
from .views import SignUpView ,AccountView,ProfileUpdateView,OrderView,UserLoginView,AuthView
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',UserLoginView,name='userlogin'),
    path('auth/',AuthView,name='auth'),
    path('account/<int:pk>/',AccountView.as_view(),name='account'),
    path('account_edit/<int:pk>/',ProfileUpdateView.as_view(),name='account_edit'),
    path('orders/',views.OrderView,name='orders'),
]
