from django.db import models
import uuid
from django.urls import reverse
from accounts.models import CustomUser

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.id])

    def __str__(self):
        return self.name
    


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_existing(self,user,review):
        if user and review:
            existing_review = self.reviews.filter(user=user).exists()
            if existing_review:
                review_limit = "Review limit reached"
                return review_limit

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.name
    
class Guitar(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'guitar'
        verbose_name_plural = 'guitars'

    def get_absolute_url(self):
        return reverse('shop:guitars', args=[self.id])

    def __str__(self):
        return self.name
    
class Bestseller(models.Model):
        id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)

        class Meta:
            ordering = ('product',)
            verbose_name = 'bestseller'
            verbose_name_plural = 'bestsellers'

        def get_absolute_url(self):
            return reverse('shop:Bestseller', args=[self.product.id, self.id])


class ProductReview(models.Model):
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="reviews")
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES,default=None)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
        
    def __str__(self):
        return self.product.name
    
    def get_rating(self):
        return self.rating