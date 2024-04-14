import uuid

from accounts.models import CustomUser
from django.db import models
from django.urls import reverse


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
    primary_image = models.ImageField(upload_to='product', blank=True)
    secondary_image1 = models.ImageField(upload_to='product', blank=True)
    secondary_image2 = models.ImageField(upload_to='product', blank=True)
    secondary_image3 = models.ImageField(upload_to='product', blank=True)
    secondary_image4 = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    discreption= models.TextField(blank=True)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    showroom = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.TextField(blank=True)
    wood = models.TextField(blank=True)
    neck = models.TextField(blank=True)
    fretboard = models.TextField(blank=True)
    frets= models.TextField(blank=True)
    pickups= models.TextField(blank=True)
    switches= models.TextField(blank=True)
    mastervol= models.TextField(blank=True)
    mastertone= models.TextField(blank=True)
    trem= models.TextField(blank=True)
    tuners= models.TextField(blank=True)
    hardware= models.TextField(blank=True)
    strings= models.TextField(blank=True)
    colour= models.TextField(blank=True)
    scale = models.IntegerField(blank=True, null=True)
    
    

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
    
    def average_rating(self):
        # Mapping for Unicode stars to corresponding integer values
        star_to_int_map = {
            "★": 1,
            "★★": 2,
            "★★★": 3,
            "★★★★": 4,
            "★★★★★": 5
        }

        # Calculate the total rating
        total_rating = sum(star_to_int_map[review.rating] for review in self.reviews.all())

        # Calculate the average rating
        if self.reviews.count() > 0:
            average= total_rating / self.reviews.count()
        else:
            average= 0
        
        stars = "★" * int(average)
        return stars
    
    def total_reviews(self):
        total_review = self.reviews.values('user').distinct().count()
        print(total_review)
        return total_review
    
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

class ProductReview(models.Model):
    RATING_CHOICES = [
        ("★", "★"),
        ("★★", "★★"),
        ("★★★", "★★★"),
        ("★★★★", "★★★★"),
        ("★★★★★", "★★★★★"),
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="reviews")
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.CharField(choices=RATING_CHOICES,default=None,max_length = 5)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
        
    def __str__(self):
        return self.product.name
    
    def get_rating(self):
        return self.rating
    
class Compare(models.Model):
    compare_id = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Compare'

    def __str__(self):
        return self.compare_id

class CompareItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    compare = models.ForeignKey(Compare, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CompareItem'
    
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
    
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    def __str__(self):
        return f'Wishlist for {self.user.username}'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
