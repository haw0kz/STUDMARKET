from django.shortcuts import render,HttpResponseRedirect
from users.forms import UserLoginForm,UserRegistrationForm,UserProfileForm
from django.urls import reverse
from django.contrib import auth,messages
from products.models import Basket
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory,Product
# Create your views here.



def login(requests):
    if requests.method == 'POST':
        form = UserLoginForm(data=requests.POST)
        if form.is_valid():
            username = requests.POST['username']
            password = requests.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user and user.is_active:
                auth.login(requests,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requests,'users/login.html', context)

def register(requests):
    if requests.method == 'POST':
        form = UserRegistrationForm(data=requests.POST)
        if form.is_valid():
            form.save()
            messages.success(requests,'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context= {'form':form}
    return render(requests,'users/register.html', context)

@login_required()
def account(requests):
    if requests.method == 'POST':
        form = UserProfileForm(data=requests.POST,files=requests.FILES,instance=requests.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:account'))
    else:
        form = UserProfileForm(instance=requests.user)
    baskets = Basket.objects.filter(user=requests.user)
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum += basket.sum()
    context = {
        'title': "Account",
        'form' : form,
        'baskets': Basket.objects.filter(user=requests.user),
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(requests,'users/account.html',context)

def logout(requests):
    auth.logout(requests)
    return HttpResponseRedirect(reverse('index'))