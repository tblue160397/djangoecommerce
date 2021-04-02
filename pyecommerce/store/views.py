from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status='Pending')
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all();
    context= {'products': products, 'cartItems':cartItems}
    return render(request, "store/store.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status='Pending')
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        items = []
        return redirect("login")
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def loginForCustomer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "store/registration/login.html", context)


def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created' + user)
            return redirect('login')
    else:
        form = CustomerForm()
    return render(request, 'store/registration/register.html', {'form': form})


def logoutForCustomer(request):
    logout(request)
    return redirect('/')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, creted = Order.objects.get_or_create(customer=customer, status='Pending')
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        return redirect('login')

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status='Pending')
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.delete()
        return redirect('cart')
    elif action == 'change':
        quantity = data['quantity']
        orderItem.quantity = quantity
        if quantity == 0:
            orderItem.delete()
            return redirect('cart')
    orderItem.save()
    if orderItem.quantity == 0:
        orderItem.delete()
        return redirect('cart')
    return JsonResponse('Item was added', safe=False)


def detailproduct(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status='Pending')
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    product = Product.objects.get(id=pk)
    comments = product.comment_set.all()
    print(comments)
    context = {'product': product, 'cartItems': cartItems, 'comments': comments}
    return render(request, 'store/detailproduct.html', context)


def addcomment(request):
    method = request.method
    customer = request.user.customer
    if method == 'POST':
        data = json.loads(request.body)
        productid = data['productId']
        action = data['action']
        content = data['content']
        print(data)
        print(method)
        product = Product.objects.get(id=productid)
        comment = Comment.objects.create(product=product, customer=customer, content=content)
        print(comment)
    return JsonResponse('Item was added', safe=False)
