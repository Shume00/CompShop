from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
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
    context = {}
    return render(request, 'CompShop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'CompShop/checkout.html', context)


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
