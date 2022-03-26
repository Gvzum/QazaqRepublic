from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:cat_name>/', category_products, name='category_products'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),

    path('favorite/', favorite_products, name='favorite'),
    path('basket/', basket, name='basket'),
    path('lookbook/', lookbook, name='lookbook'),
    path('search/', search, name='search'),

    path('test/<slug:slug>/', test, name='test'),
    path('update_favs/<slug:slug>/', click_like, name='click_like')
]