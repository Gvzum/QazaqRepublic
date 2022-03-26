from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import *

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

def get_jean(request, slug):
    jean = Product.objects.get(slug=slug)
    print(jean)
    return HttpResponse('Jeans are there')

# class GetOneJeansView(DetailView):
#     model = Product

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
    context = {
        'title': 'Search'
    }
    if request.method == 'POST':
        context['products'] = Product.objects.filter(name__contains=request.POST['search'], category__name__contains=request.POST['search'])
        print(context['products'])

    return render(request, 'bastama/search.html', context)

def lookbook(request):
    return render(request, 'bastama/lookbook.html')

def test(request):
    return render(request, 'bastama/components/test.html')