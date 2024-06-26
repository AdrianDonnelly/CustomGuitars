from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage,PageNotAnInteger
from .models import Category, Product, Guitar, ProductReview, Compare, CompareItem,Brand,Wishlist,WishlistItem
from shop.forms import ProductReviewForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'home.html')


def prod_list(request, category_id=None, brand_id=None):
    
    category = None
    brand = None
    products = Product.objects.filter(available=True)

    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

   
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        products = products.filter(brand=brand)

    
    paginator = Paginator(products, 20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    

    brands = Brand.objects.all()
    return render(request, 'products/catagories.html', {'category': category, 'brand': brand, 'prods': products, 'brands': brands})



def product_detail(request, category_id, product_id):
   
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    category = Category.objects.all()
    brand = product.brand
    reviews = product.reviews.all()
    average_rating = product.average_rating()
    total_reviews = product.total_reviews()
    featured_products = None
    product_category = None
    page_obj = None

    try:
        review_instance = get_object_or_404(ProductReview, product=product, user=request.user)

    except:
        review_instance = None

    p = Paginator(reviews, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(4)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

   
    if category is not None:
        product_category = get_object_or_404(Category, id=category_id)
        featured_products = Product.objects.filter(category=product_category, featured=True, available=True)

    existing_review = product.get_existing(user=request.user, review=review_instance)

    
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
           
            reviews = product.reviews.all()
            form = ['Thank you for submitting a review']
    else:
        form = ProductReviewForm()

    return render(request, 'products/product.html', {'product': product, 'reviews': reviews,
                                                     'form': form, 'existing_review': existing_review,
                                                     'featured': featured_products, 'product_category': category,
                                                     'page_obj': page_obj, 'average_rating': average_rating,
                                                     'total_reviews': total_reviews, 'brand': brand})


def guitars(request):
    
    guitars = Guitar.objects.filter(available=True)
    return render(request, 'products/guitars.html', {'guitars': guitars})




def view_images(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/view_image.html', {'product': product})

def featured(request, category=None):
    categories = Category.objects.all()
    featured_products = []

    if category:
        selected_category = get_object_or_404(Category, name=category)
        featured_products = Product.objects.filter(category=selected_category, featured=True, available=True)

    return render(request, 'home.html', {'categories': categories, 'featured': featured_products, 'selected_category': category})
 
def _compare_id(request):
    compare = request.session.session_key
    if not compare:
        compare = request.session.create()
    return compare

def add_compare(request, product_id):
    product = Product.objects.get(id=product_id)
    error_message=None
    
    try:
        compare= Compare.objects.get(compare_id=_compare_id(request))
    except Compare.DoesNotExist:
        compare = Compare.objects.create(compare_id=_compare_id(request))
        compare.save()
        
    if CompareItem.objects.filter(compare=compare).count() >= 3:
        error_message ="You can only compare up to three items."
        request.session['error_message'] = error_message
        return redirect('shop:compare_detail')
        
    try:
        compare_item = CompareItem.objects.get(product=product, compare=compare)
        compare_item.save()
    
    except CompareItem.DoesNotExist:
        compare_item = CompareItem.objects.create(product=product,compare=compare)
        
    if error_message:
        request.session['error_message'] = error_message
        
    return redirect('shop:compare_detail')

def compare_detail(request, total=0, counter=0, compare_items = None):
    error_message = request.session.pop('error_message', None)
    try:
        compare = Compare.objects.get(compare_id=_compare_id(request))
        compare_items = CompareItem.objects.filter(compare=compare, active=True)
        for compare_item in compare_items:
            counter += compare_item.quantity
    except:
        ObjectDoesNotExist
        pass
        
    return render(request, 'products/compare.html', { 'compare_items':compare_items, 'error_message':error_message})

def compare_remove(request, product_id):
    compare= Compare.objects.get(compare_id=_compare_id(request))
    product = get_object_or_404(Product, id=product_id)
    compare_item = CompareItem.objects.get(product=product, compare=compare)
    compare_item.delete()
    return redirect('shop:compare_detail')



@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, item_created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

    if item_created:
        message = f'{product.name} added to your wishlist.'
    else:
        message = f'{product.name} is already in your wishlist.'

    return redirect('shop:wishlist_detail')

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist_item = get_object_or_404(WishlistItem, wishlist=wishlist, product=product)
    wishlist_item.delete()

    return redirect('shop:wishlist_detail')

@login_required
def wishlist_detail(request):
   
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    wishlist_items = wishlist.items.all()
    
    return render(request, 'products/wishlist.html', {'wishlist': wishlist, 'wishlist_items': wishlist_items,'show_account_sidebar': True})