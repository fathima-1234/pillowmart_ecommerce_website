from django.urls import path
from . import views

urlpatterns = [
# pages
path('cart',views.cart, name='cart'), 
path('wishlist',views.wishlist,name='wishlist'),
path('checkout2',views.checkout2,name='checkout2'),


# fuctions
path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
path('RemoveFromCart/<int:id>/',views.RemoveFromCart,name='RemoveFromCart'),
path('CartQuantity/<int:id>/<str:action>/',views.CartQuantity,name='CartQuantity'),
path('addToWishlist/<int:id>/',views.addToWishlist,name='addToWishlist'),
path('RemoveFromWishlist/<int:id>/',views.RemoveFromWishlist,name='RemoveFromWishlist'),
]