from django.urls import path
from .views import SignUpView, AccountView, ProfileUpdateView, OrderView, UserLoginView, OtpView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('userlogin/', UserLoginView, name='userlogin'),
    path('otp/', OtpView, name='otp'),
    path('account/<int:pk>/', AccountView.as_view(), name='account'),
    path('account_edit/<int:pk>/', ProfileUpdateView.as_view(), name='account_edit'),
    path('orders/', OrderView, name='orders'), 
]
