from django.db import models
import uuid
from django.urls import reverse
from accounts.models import CustomUser
from shop.models import Category, Product


class Wishlist(models.Model):
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        available = models.BooleanField(default=True)

        class Meta:
            ordering = ('name',)
            verbose_name = 'wishlist'

        def get_absolute_url(self):
            return reverse("shop:Wishlist")


            