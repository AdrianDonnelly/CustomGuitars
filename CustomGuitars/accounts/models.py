from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(null = True, blank = True)
    email = models.EmailField(max_length=254,unique=True)
    secret_key = models.CharField(max_length=16, null=True) 
    phone_number = models.BigIntegerField(null=True)
    def get_absolute_url(self):
        return reverse('accounts:account', args=[str(self.id)])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
    )
    secret_key = models.CharField(max_length=16, null=True)

    
    def __str__(self):
        return str(self.user)
    
    
    