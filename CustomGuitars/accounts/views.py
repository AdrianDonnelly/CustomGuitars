from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView ,UpdateView
from django.contrib.auth.models import Group,User
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser, Profile
from django.contrib.auth import authenticate, get_user_model
from .utils import send_otp
from datetime import datetime
import pyotp
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('userlogin')
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
    
def OtpView(request):
    error_message = None
    user = request.session.get('otp_user')
    
    if user is not None:
        User = get_user_model()
        user = get_object_or_404(User, id=user)
    
    if request.method == "POST":
        otp = request.POST.get('otp', '')
        
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']
        
        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)
            
            if valid_until>datetime.now():
                totp = pyotp.TOTP(otp_secret_key,interval=60)
                if totp.verify(otp):
                    login(request,user)
                    return redirect('shop:home')
                
                    
                    
                    
                    
                else:
                    error_message = "invalid One time password token"
            else:
                error_message = "otp token has expired"
        else:
            error_message = "something went wrong"
                    
                    

    return render(request,'registration/otp.html',{'error_message': error_message})
    
    
def UserLoginView(request):
    error_message=None
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            request.session['otp_user'] = user.id
            send_otp(request)
            return redirect('accounts:otp')
            
        
        else:
            error_message = "Invalid Username or Password"
        
    return render(request, 'registration/userlogin.html', {'error_message': error_message})

        


    
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

