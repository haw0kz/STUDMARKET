from django.shortcuts import render,HttpResponseRedirect
from products.models import ProductCategory,Product,Basket
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(requests):
    context = {
        'categories': ProductCategory.objects.all(),
        'title': "StudMarket",
    }
    return render(requests,'products/index.html',context)


def about(requests):
    context = {

        'categories': ProductCategory.objects.all(),
        'title': "About us"
    }
    return render(requests,'products/about.html',context)


def contact(requests):
    context = {
        'categories': ProductCategory.objects.all(),
        'title': "Contact"
    }
    return render(requests,'products/contact.html',context)

def products(requests,category_id=None):
    context = {
        'title': "Products",
        'categories' : ProductCategory.objects.all(),
    }
    if category_id:
        context.update({'products':Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})
    return render(requests,'products/product.html',context)

def prodvoz(requests):
    context = {
        'title': "Products",
        'categories' : ProductCategory.objects.all(),
        'products':Product.objects.all().order_by('price'),
    }
    return render(requests,'products/product.html',context)

def prodyb(requests):
    context = {
        'title': "Products",
        'categories' : ProductCategory.objects.all(),
        'products': Product.objects.all().order_by('-price'),
    }
    return render(requests,'products/product.html',context)

@login_required
def basket_add(requests,product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=requests.user,product=product)

    if not baskets.exists():
        Basket.objects.create(user=requests.user,product=product,quantity=1)
        return HttpResponseRedirect(requests.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(requests.META.get('HTTP_REFERER'))

@login_required
def basket_delete(requests,id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(requests.META.get('HTTP_REFERER'))
