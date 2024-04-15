from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','dob','phone_number')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['dob'].widget.attrs['placeholder'] = 'Date of birth (YYYY-MM-DD)'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone number'
    
class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = CustomUser
        fields = ('username','email','phone_number')

