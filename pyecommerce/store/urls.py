from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login', views.loginForCustomer, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logoutForCustomer, name='logout'),
    path('update_item/', views.updateItem, name='update_item'),
]
