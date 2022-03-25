from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import render

from .models import *
from .utils import *

app_name = 'bastama'


def index(request):
    return render(request, 'bastama/index.html', {'title': 'Qazaq Republic'})


def basket(request):
    basket_data = get_basket_data(request)  # Getting all products from basket
    print(basket_data)
    return render(request, 'bastama/basket.html')


def favorite_products(request):
    products = get_favorite_products(request)
    print(products[0].product.name)
    return HttpResponse('Favorite page')


def search(request):
    context = {
        'title': 'Search'
    }
    if request.method == 'POST':
        context['products'] = Product.objects.filter(name__contains=request.POST['search'],
                                                     category__name__contains=request.POST['search'])

    return render(request, 'bastama/search.html', context)


def lookbook(request):
    return render(request, 'bastama/lookbook.html')


def category_products(request, cat_name):
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



