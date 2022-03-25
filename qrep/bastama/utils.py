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

def basket_data(request):
    if request.user.is_authenticated:
        user = request.user
        customer, _ = Customer.objects.get_or_create(user=user)
        print(customer)
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_basket_total
        # print(cartItems)
        # print(customer)
    else:
        pass
