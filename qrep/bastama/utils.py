from .models import Order, Customer

SIDEBAR_SUBCATEGORY_PRODUCTS = {
    'jeans': [
        ('jeans', 'Jeans'),
        ('shalbars', 'Shalbar')
    ],
    'jeide': [
        ('jeideler', 'Jeide'),
        ('kenjeideler', 'Kenjeide'),
        ('birjeideler', 'Burjeide')
    ],
    'qosymsha': [
        ('betperdeler', 'Betperde'),
        ('botelkeler', 'Botelke'),
        ('keseler', 'Kese'),
        ('qalpaktar', 'Qalpaq'),
        ('panamalar', 'Panama'),
        ('kepkalar', 'Kepka'),
        ('somkeler', 'Somke'),
    ],
    'gift': [

    ]
}


def get_or_create_customer(user):
    customer, _ = Customer.objects.get_or_create(user=user)
    return customer


def get_basket_data(request):
    if request.user.is_authenticated:
        customer = get_or_create_customer(request.user)
        print(customer)
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_basket_total
    else:
        pass

    return {'cartItems': cartItems, 'items': items, 'order': order}


def get_favorite_products(request):
    if request.user.is_authenticated:
        customer = get_or_create_customer(request.user)
        favorite_products = customer.favors_set.all()
    else:
        favorite_products = []
        pass

    return favorite_products
