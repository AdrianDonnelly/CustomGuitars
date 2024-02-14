from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    
class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
    )
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(null = True, blank = True)
    email = models.EmailField(max_length=254, )
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("show_profile", args=[str(self.id)])
    