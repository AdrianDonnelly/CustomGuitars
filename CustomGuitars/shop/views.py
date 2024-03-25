from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product , Guitar, ProductReview, Compare,CompareItem
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from shop.forms import ProductReviewForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'home.html')

def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)

    paginator = Paginator(products, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/catagories.html', {'category': category, 'prods': products})


def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    reviews = product.reviews.all()
    try:
        review_instance = get_object_or_404(ProductReview,product=product,user=request.user)
    except:
        review_instance=None
        
    existing_review = product.get_existing(user=request.user,review=review_instance)
    
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid ():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
            # Refresh reviews after submitting the form
            reviews = product.reviews.all()
            form = ['Thank you for submitting a review']
    else:
        form = ProductReviewForm()

    return render(request, 'products/product.html', {'product': product, 'reviews': reviews , 'form':form ,'existing_review':existing_review})

def guitars(request):
    guitars = Guitar.objects.filter(available=True)
    return render(request, 'products/guitars.html', {'guitars': guitars})



def featured(request, category=None):
    categories = Category.objects.all()
    featured_products = []

    if category:
        selected_category = get_object_or_404(Category, name=category)
        featured_products = Product.objects.filter(category=selected_category, featured=True, available=True)

    print("Featured Products:", featured_products)
    return render(request, 'home.html', {'categories': categories, 'featured': featured_products, 'selected_category': category})
 
def _compare_id(request):
    compare = request.session.session_key
    if not compare:
        compare = request.session.create()
    return compare

def add_compare(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        compare= Compare.objects.get(compare_id=_compare_id(request))
    except Compare.DoesNotExist:
        compare = Compare.objects.create(compare_id=_compare_id(request))
        compare.save()
        
    try:
        compare_item = CompareItem.objects.get(product=product, compare=compare)
        compare_item.save()
    except CompareItem.DoesNotExist:
        compare_item = CompareItem.objects.create(product=product,compare=compare)
    return redirect('shop:compare_detail')

def compare_detail(request, total=0, counter=0, compare_items = None):
    try:
        compare = Compare.objects.get(compare_id=_compare_id(request))
        compare_items = CompareItem.objects.filter(compare=compare, active=True)
        for compare_item in compare_items:
            counter += compare_item.quantity
    except:
        ObjectDoesNotExist
        pass
        
    return render(request, 'products/compare.html', { 'compare_items':compare_items})

def compare_remove(request, product_id):
    compare= Compare.objects.get(compare_id=_compare_id(request))
    product = get_object_or_404(Product, id=product_id)
    compare_item = CompareItem.objects.get(product=product, compare=compare)
    compare_item.delete()
    return redirect('shop:compare_detail')


    