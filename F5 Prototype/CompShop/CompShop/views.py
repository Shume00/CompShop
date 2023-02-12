from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'CompShop/main.html', context)

def store(request):
    context = {}
    return render(request, 'CompShop/store.html', context)

def cart(request):
    context = {}
    return render(request, 'CompShop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'CompShop/checkout.html', context)

