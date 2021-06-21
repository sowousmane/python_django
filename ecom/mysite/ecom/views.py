from django.http.response import JsonResponse
from .models import *
from django.shortcuts import render, redirect
import json
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_log, logout

# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accoutn was created for' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)


def login(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username=username, password= password)

        if user is not None:
            auth_log(response, user)
            return redirect('store')
        else:
            messages.info(response, 'email or password incorrect' )
    context = {}
    return render(response, 'registration/login.html', context)


def logoutU(response):
    logout(response)
    return redirect('login')

def store(response):
    if response.user.is_authenticated:
        customer = response.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()
        cartItems = order.total_cart_items
    else:
        items = []
        order = {'total_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['total_cart_items']
    
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(response, 'ecom/store.html', context)


# cart

def cart(response):
    if response.user.is_authenticated:
        customer = response.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()
        cartItems = order.total_cart_items
    else:
        items = []
        order = {'total_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['total_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(response, 'ecom/cart.html', context)


# checkout
def checkout(response):
    if response.user.is_authenticated:
        customer = response.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem.all()
        cartItems = order.total_cart_items
    else:
        items = []
        order = {'total_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['total_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(response, 'ecom/checkout.html', context)


def viewart(response):    
        
    products = Product.objects.all()
    return render(response, 'ecom/viewart.html', {'products':products})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderedItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
           orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0 :
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
