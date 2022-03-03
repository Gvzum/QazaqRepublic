from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('jeans/', jeans, name='jeans'),
    path('jeide/', jeide, name='jeide'),
    path('qosymsha/', qosymsha, name='qosymsha'),
    path('gift/', gift, name='gift'),
    path('basket/', basket, name='basket'),
    path('search/', search, name='search'),
    path('test/', test, name='test'),
]