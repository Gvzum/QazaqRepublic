from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import *
from .utils import *

app_name = 'bastama'

def index(request):
    if request.method == "POST":
        message_email = request.POST['message-email']
        message_name = request.POST['message-name']
        message = request.POST['message']

        send_mail(
            'message from ' + message_name + ',' + message_email,
            message,
            message_email,
            ['200103223@stu.sdu.edu.kz'],
        )
        return redirect("bastama:home")


      #  return render(request, 'bastama/index.html', {'message_name':message_name},{'title': 'Qazaq Republic'})

    else: return render(request, 'bastama/index.html', {'title': 'Qazaq Republic'})
    if request.method == "GET":
        message_email = request.GET['message-ems']

        send_mail(
            'subscription from ' + message_ems,
            ['200103223@stu.sdu.edu.kz'],
        )
        return redirect("bastama:home")


      #  return render(request, 'bastama/index.html', {'message_name':message_name},{'title': 'Qazaq Republic'})

    else: return render(request, 'bastama/index.html', {'title': 'Qazaq Republic'})

def gift(request):
    return render(request, 'bastama/gift.html')

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
        context['products'] = Product.objects.filter(name__contains=request.POST['search'], category__name__contains=request.POST['search'])
        print(context['products'])

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


def test(request, slug):
    context = {'title': 'test'}
    product = Product.objects.get(slug=slug)
    print(product)
    context['product'] = product

    return render(request, 'bastama/components/test.html', context)


def click_like(request, slug):
    customer = get_or_create_customer(request.user)
    favorite_product = Product.objects.get(slug=slug)

    favorite, is_fav = is_favorite_of_customer(customer, favorite_product)

    print(favorite)
    print(is_fav)

    if is_fav:
        favorite.delete()
    else:
        Favors.objects.create(customer=customer, product=favorite_product)

    return redirect('bastama:test', slug=slug)
