from django.views.generic import *
from django.shortcuts import render

from .models import *

app_name = 'bastama'

def index(request):
    return render(request, 'bastama/index.html')
#
# def jeans(request):
#     return render(request, 'bastama/jeans.html')

# def jeide(request):
#     return render(request, 'bastama/jeide.html')

class JeansView(ListView):
    model = Product
    template_name = 'bastama/jeans.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Jeansilar'
        context['jeans'] = Product.objects.filter(category__name='Jeans')
        context['shalbars'] = Product.objects.filter(category__name='Shalbar')

        return context

class JeideView(ListView):
    model = Product
    template_name = 'bastama/jeide.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Jeideler'
        context['jeideler'] = Product.objects.filter(category__name='Jeide')
        context['kenjeideler'] = Product.objects.filter(category__name='Kenjeide')
        context['birjeideler'] = Product.objects.filter(category__name='Burjeide')

        return context

class QosymshaView(ListView):
    model = Product
    template_name = 'bastama/qosymsha.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Qosymsha'
        context['betperdeler'] = Product.objects.filter(category__name='Betperde')
        context['botelkeler'] = Product.objects.filter(category__name='Botelke')
        context['keseler'] = Product.objects.filter(category__name='Kese')
        context['qalpaktar'] = Product.objects.filter(category__name='Qalpaq')
        context['panamalar'] = Product.objects.filter(category__name='Panama')
        context['kepkalar'] = Product.objects.filter(category__name='Kepka')
        context['somkeler'] = Product.objects.filter(category__name='Somke')

        return context

# def qosymsha(request):
#     return render(request, 'bastama/qosymsha.html')

def gift(request):
    return render(request, 'bastama/gift.html')

def basket(request):
    return render(request, 'bastama/basket.html')

def search(request):
    return render(request, 'bastama/search.html')

def lookbook(request):
    return render(request, 'bastama/lookbook.html')

def test(request):
    return render(request, 'bastama/components/test.html')