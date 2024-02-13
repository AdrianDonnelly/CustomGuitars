from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView ,UpdateView 
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        try:
            customer_group = Group.objects.get(name='Customer')
        except Group.DoesNotExist:
            customer_group = Group.objects.create(name='Customer')

        signup_user = form.save()
        username = form.cleaned_data.get('username')
        signup_user = CustomUser.objects.get(username=username)
        customer_group.user_set.add(signup_user)
        return super().form_valid(form)

class AccountView(UpdateView):
    model = CustomUser
    success_url = reverse_lazy('account_edit')
    form_class = CustomUserChangeForm
    template_name = 'accounts/account.html'

    def get_object(self, queryset=None):
        return self.request.user

class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('account')
    template_name = 'accounts/account_edit.html'  
    
    def get_object(self, queryset=None):
        return self.request.user
    
def OrderView(request):
    return render(request, 'accounts/orders.html', {'orders':OrderView})

