from django.urls import path,include
from .views import SignUpView, AccountView, ProfileUpdateView, OrderView, UserLoginView, OtpView, Setup_2FAView 
from shop.views import wishlist_detail

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('userlogin/', UserLoginView, name='userlogin'),
    path('otp/', OtpView, name='otp'),
    path('account/<int:pk>/', AccountView.as_view(), name='account'),
    path('setup_2FA/<int:pk>/',Setup_2FAView.as_view(),name='setup_2FA'),
    path('account_edit/<int:pk>/', ProfileUpdateView.as_view(), name='account_edit'),
    path('orders/', OrderView, name='orders'), 
    path('wishlist/', include('shop.urls')),
]
