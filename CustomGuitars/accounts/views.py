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

        signup_user = form.save()
        username = form.cleaned_data.get('username')
        signup_user = CustomUser.objects.get(username=username)
        customer_group.user_set.add(signup_user)
        return super().form_valid(form)
    
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'accounts/account_edit.html'  
    form_class = CustomUserChangeForm
    def account_view(request, pk):
        profile = get_object_or_404(Profile, user__pk=pk)
        
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse('show_profile', args=[str(self.object.id)])
    
    
class AccountView(DetailView):
    model = Profile
    template_name = 'accounts/account.html'
    account_edit_url= reversed("account_edit")
    
def OrderView(request):
    return render(request, 'accounts/orders.html', {'orders':OrderView})

