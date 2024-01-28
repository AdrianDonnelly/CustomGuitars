from shop.models import Category, Product

def menu_links(request):
    links = Category.objects.guitars()
    return{'links':links}