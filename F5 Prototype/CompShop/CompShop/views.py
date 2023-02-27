from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
import json
from .models import *
from .forms import *


def index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'CompShop/main.html', context)


def store(request):
    products = Product.objects.all()
    productimages = ProductImages.objects.all()
    context = {'products': products,
               'productimages': productimages}
    return render(request, 'CompShop/store.html', context)


def cart(request):
    user = request.user
    itemsincart = Productisinsc.objects.filter(scid=user.userid)
    context = {'user': user,
               'itemsincart': itemsincart}
    return render(request, 'CompShop/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productID']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    currentUser = request.user
    customer = currentUser.userid
    product = Product.objects.get(productid=productId)
    cart, created = ShoppingCart.objects.get_or_create(customerid=customer, scid=customer)
    cartItem, created = Productisinsc.objects.get_or_create(productid=product, scid=cart)

    if action == 'add':
        if cartItem.quantity is None:
            cartItem.quantity = 1
        else:
            cartItem.quantity = (cartItem.quantity + 1)
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)

    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()

    return JsonResponse('Item was added', safe=False)


def checkout(request):
    context = {}
    return render(request, 'CompShop/checkout.html', context)

def myorders(request):
    user = request.user
    orders = Orders.objects.filter(customerid=user.userid)
    productsinorder = Orderhasproduct.objects.all()
    context = {'orders': orders,
               'products': productsinorder}
    return render(request, 'CompShop/orders.html', context)


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.success(request, 'There was an error logging in. Try again!')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', context)


def logout_user(request):
    context = {}
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('store')


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('store')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
