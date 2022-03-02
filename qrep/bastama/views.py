from django.http import HttpResponse
from django.shortcuts import render

app_name = 'bastama'

def index(request):
    return render(request, 'bastama/index.html')

def jeans(request):
    return render(request, 'bastama/jeans.html')