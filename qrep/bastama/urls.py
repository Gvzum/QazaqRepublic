from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('jeans/', JeansView.as_view(), name='jeans'),
    path('jeide/', JeideView.as_view(), name='jeide'),
    path('qosymsha/', QosymshaView.as_view(), name='qosymsha'),
    path('gift/', gift, name='gift'),
    path('basket/', basket, name='basket'),
    path('search/', search, name='search'),
    path('lookbook/', lookbook, name='lookbook'),
    path('test/', test, name='test'),
]