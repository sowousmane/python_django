from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("lougout/", views.logoutU, name="logout"),
    path("viewart/", views.viewart, name="viewart"),
  

]