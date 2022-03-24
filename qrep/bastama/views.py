from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import render

from .models import *
from .utils import SIDEBAR_SUBCATEGORY_PRODUCTS, basket_data

app_name = 'bastama'

def index(request):
    return render(request, 'bastama/index.html', {'title': 'Qazaq Republic'})

def basket(request):
    return render(request, 'bastama/basket.html')

def search(request):
    context = {
        'title': 'Search'
    }
    if request.method == 'POST':
        context['products'] = Product.objects.filter(name__contains=request.POST['search'], category__name__contains=request.POST['search'])

    return render(request, 'bastama/search.html', context)

def lookbook(request):
    return render(request, 'bastama/lookbook.html')

def show_category_products(request, cat_name):

    basket_data(request)

    context = {}
    template_url = 'bastama/'
    products_from_subcategory = SIDEBAR_SUBCATEGORY_PRODUCTS[cat_name]

    if cat_name == 'jeans':
        template_url += 'jeans.html'
    elif cat_name == 'jeide':
        template_url += 'jeide.html'
    elif cat_name == 'qosymsha':
        template_url += 'qosymsha.html'
    elif cat_name == 'gift':
        template_url += 'gift.html'

    for product_tupple in products_from_subcategory:
        context_key = product_tupple[0]
        value_to_filter = product_tupple[1]
        context['title'] = value_to_filter
        context[context_key] = Product.objects.filter(category__name=value_to_filter)

    return render(request, template_url, context)

def product_detail(request, slug):
    print(slug)
    product = Product.objects.get(slug=slug)
    print(product)
    return HttpResponse('There you are')

def get_favorite_products(request):
    print(request.user)
    favs = Favors.objects.filter(customer=request.user)
    print(favs)
    return HttpResponse('Favorite page')