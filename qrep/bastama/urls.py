from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('jeans/', jeans, name='jeans'),
    path('jeide/', jeide, name='jeide'),
    path('test/', test, name='test'),
]