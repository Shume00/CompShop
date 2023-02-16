from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    context = {}
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
