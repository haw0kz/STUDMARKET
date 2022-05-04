from django.shortcuts import render

from products.models import ProductCategory,Product
# Create your views here.

def index(requests):
    context = {
        'title': "StudMarket"
    }
    return render(requests,'products/index.html',context)

def about(requests):
    context = {
        'title': "About us"
    }
    return render(requests,'products/about.html',context)


def contact(requests):
    context = {
        'title': "Contact"
    }
    return render(requests,'products/contact.html',context)

def products(requests):
    context = {
        'title': "Products",
        'categories' : ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(requests,'products/product.html',context)

