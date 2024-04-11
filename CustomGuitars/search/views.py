from django.views.generic import ListView
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from shop.models import Product, Category


class SearchResultsListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category_name = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        queryset = Product.objects.all()

        if query:
            queryset = queryset.filter(Q(name__icontains=query))

        if category_name:
            
            category_name_lower = category_name.lower()
            
            queryset = queryset.filter(category__name__iexact=category_name_lower)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context