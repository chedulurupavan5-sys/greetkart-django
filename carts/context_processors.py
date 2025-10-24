from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    # don't show cart count in admin
    if 'admin' in request.path:
        return {}

    cart_count = 0
    cart = Cart.objects.filter(cart_id=_cart_id(request)).first()  # returns Cart or None

    if cart:
        cart_items = CartItem.objects.filter(cart=cart).only('quantity')
        for ci in cart_items:
            cart_count += ci.quantity

    return {'cart_count': cart_count}
