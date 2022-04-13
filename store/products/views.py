from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests,'products/index.html')

def about(requests):
    return render(requests,'products/about.html')

def blogdetail(requests):
    return render(requests,'products/blog-detail.html')

def contact(requests):
    return render(requests,'products/contact.html')

def product(requests):
    return render(requests,'products/product.html')

def productdetail(requests):
    return render(requests,'products/product-detail.html')

def shopingcart(requests):
    return render(requests,'products/shoping-cart.html')

def account(requests):
    return render(requests,'products/account.html')