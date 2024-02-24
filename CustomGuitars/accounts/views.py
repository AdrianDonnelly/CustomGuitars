from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView ,UpdateView
from django.contrib.auth.models import Group
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser, Profile

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        try:
            customer_group = Group.objects.get(name='Customer')
        except Group.DoesNotExist:
            customer_group = Group.objects.create(name='Customer')

        user = form.save()
        username = form.cleaned_data.get('username')
        user = CustomUser.objects.get(username=username)
        customer_group.user_set.add(user)
        Profile.objects.create(
            user=user
        )
        return super().form_valid(form)
    
def UserLoginView(request):
    error_message = "Login Error"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('login')
        
        else:
            return render(request,'login.html')

    
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'accounts/account_edit.html'  
    form_class = CustomUserChangeForm
        
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs['pk'])
    
    def get_object(self, queryset=None):
        return self.request.user
    
    
    
    
class AccountView(DetailView):
    model = Profile
    template_name = 'accounts/account.html'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs['pk'])

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_edit_url'] = reverse_lazy('accounts:account_edit', kwargs={'pk': self.object.user.id})
        return context

    
def OrderView(request):
    return render(request, 'accounts/orders.html', {'orders':OrderView})

def Otp(request):
    username 
