from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login', views.loginForCustomer, name="login"),
    path('register', views.register, name="register"),
    path('customerprofile', views.customerprofile, name='customerprofile'),
    path('logout', views.logoutForCustomer, name='logout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('product/<int:pk>', views.detailproduct, name='detailproduct'),
    path('add_comment/', views.addcomment, name='addcomment'),
    path('update_customer_inf/', views.updateEmail, name="update_customer_inf"),
]
