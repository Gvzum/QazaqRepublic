from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:cat_name>/', show_category_products, name='category_products'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),

    # path('jeans/', JeansView.as_view(), name='jeans'),
    # path('jeide/', JeideView.as_view(), name='jeide'),
    # path('qosymsha/', QosymshaView.as_view(), name='qosymsha'),
    # path('gift/', gift, name='gift'),
    path('basket/', basket, name='basket'),
    path('lookbook/', lookbook, name='lookbook'),
    path('search/', search, name='search'),

    path('favorite/', get_favorite_products, name='favorites')
]