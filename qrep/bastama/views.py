from django.http import HttpResponse
from django.shortcuts import render

app_name = 'bastama'

def index(request):
    return render(request, 'bastama/index.html')

def jeans(request):
    return render(request, 'bastama/jeans.html')

def jeide(request):
    return render(request, 'bastama/jeide.html')

def qosymsha(request):
    return render(request, 'bastama/qosymsha.html')

def gift(request):
    return render(request, 'bastama/gift.html')

def basket(request):
    return render(request, 'bastama/basket.html')

def search(request):
    return render(request, 'bastama/search.html')

def test(request):
    return render(request, 'bastama/components/test.html')