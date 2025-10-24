"""from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
]


from django.urls import path
from . import views   # or: from .views import Cart, cart

urlpatterns = [
    # If class-based:
    # path("", views.Cart.as_view(), name="cart"),

    # If function-based:
   path("", views.cart, name="cart"),
   path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
   path('remove_cart/<int:product_id>/<int:cart_tem_id>/', views.remove_cart, name='remove_cart'),
   path('remove_cart_item/<int:product_id>/<int:cart_tem_id>/',views.remove_cart_item,name='remove_cart_item'),
]

"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add_cart/<int:product_id>/", views.add_cart, name="add_cart"),
    path("remove_cart/<int:product_id>/<int:cart_item_id>/", views.remove_cart, name="remove_cart"),
    path("remove_cart_item/<int:product_id>/<int:cart_item_id>/", views.remove_cart_item, name="remove_cart_item"),
   # path("checkout/", views.checkout, name="checkout"),  # only if you actually have this view
]
