from .models import Category, Product

def menu_links(request):
    links = Category.objects.all()
    return{'links':links}

def acount_sidebar(request):
    return {
        'show_account_sidebar': False,  
    }